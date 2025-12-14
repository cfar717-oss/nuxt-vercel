#!/usr/bin/env python3
"""
Flowgram Validator v0.1
Validates flowgram YAML files against Freedomation specification.
"""

import sys
import yaml
from pathlib import Path


class FlowgramValidator:
    def __init__(self, flowgram_path):
        self.flowgram_path = Path(flowgram_path)
        self.errors = []
        self.warnings = []
        self.repo_root = self.flowgram_path.parent.parent.parent

    def validate(self):
        """Run all validations"""
        print(f"Validating flowgram: {self.flowgram_path}")
        print("-" * 60)

        # Load YAML
        try:
            with open(self.flowgram_path) as f:
                self.fg = yaml.safe_load(f)
        except Exception as e:
            self.error(f"Failed to parse YAML: {e}")
            return False

        # Run validations
        self.validate_required_fields()
        self.validate_artifacts()
        self.validate_nodes()
        self.validate_edges()
        self.validate_gates()
        self.validate_outputs()

        # Report results
        self.report()

        return len(self.errors) == 0

    def validate_required_fields(self):
        """Check top-level required fields"""
        required = ['fg_id', 'version', 'human_title', 'modes', 'nodes', 'edges', 'outputs']
        for field in required:
            if field not in self.fg:
                self.error(f"Missing required field: {field}")

    def validate_artifacts(self):
        """Validate all artifact references exist as schema files"""
        artifacts_dir = self.repo_root / 'freedomation' / 'artifacts'

        # Collect all artifact references
        artifact_refs = set()

        # From top-level artifacts list
        if 'artifacts' in self.fg:
            artifact_refs.update(self.fg['artifacts'])

        # From initial_artifacts
        if 'initial_artifacts' in self.fg:
            if 'required' in self.fg['initial_artifacts']:
                artifact_refs.update(self.fg['initial_artifacts']['required'])
            if 'optional' in self.fg['initial_artifacts']:
                artifact_refs.update(self.fg['initial_artifacts']['optional'])

        # From nodes
        if 'nodes' in self.fg:
            for node in self.fg['nodes']:
                if 'inputs_required' in node:
                    artifact_refs.update(node['inputs_required'])
                if 'inputs_optional' in node:
                    artifact_refs.update(node['inputs_optional'])
                if 'outputs_primary' in node:
                    artifact_refs.update(node['outputs_primary'])
                if 'outputs_secondary' in node:
                    artifact_refs.update(node['outputs_secondary'])

        # From edges
        if 'edges' in self.fg:
            for edge in self.fg['edges']:
                if 'artifact_type' in edge:
                    artifact_refs.add(edge['artifact_type'])

        # From gates
        if 'gates' in self.fg:
            for gate in self.fg['gates']:
                if 'applies_to' in gate:
                    artifact_refs.update(gate['applies_to'])

        # From outputs
        if 'outputs' in self.fg:
            artifact_refs.update(self.fg['outputs'])

        # Check each artifact has a schema file
        for artifact in artifact_refs:
            schema_file = artifacts_dir / f"{artifact}.yaml"
            if not schema_file.exists():
                self.error(f"Artifact schema missing: {artifact} (expected at {schema_file})")

    def validate_nodes(self):
        """Validate node structure"""
        if 'nodes' not in self.fg:
            return

        node_ids = set()
        for i, node in enumerate(self.fg['nodes']):
            # Check required fields
            required = ['node_id', 'kb_ref', 'human_title', 'inputs_required', 'outputs_primary']
            for field in required:
                if field not in node:
                    self.error(f"Node {i}: missing required field '{field}'")

            # Check node_id uniqueness
            if 'node_id' in node:
                if node['node_id'] in node_ids:
                    self.error(f"Duplicate node_id: {node['node_id']}")
                node_ids.add(node['node_id'])

            # Check KB reference format
            if 'kb_ref' in node:
                kb_ref = node['kb_ref']
                if not kb_ref.startswith('KB-'):
                    self.error(f"Node {node.get('node_id', i)}: kb_ref should start with 'KB-' (got: {kb_ref})")

    def validate_edges(self):
        """Validate edge structure"""
        if 'edges' not in self.fg:
            self.warning("No edges defined")
            return

        # Get all node_ids
        node_ids = set()
        if 'nodes' in self.fg:
            node_ids = {n['node_id'] for n in self.fg['nodes'] if 'node_id' in n}

        for i, edge in enumerate(self.fg['edges']):
            # Check required fields
            required = ['from', 'to', 'artifact_type']
            for field in required:
                if field not in edge:
                    self.error(f"Edge {i}: missing required field '{field}'")

            # Check from/to reference valid nodes
            if 'from' in edge and edge['from'] not in node_ids:
                self.error(f"Edge {i}: 'from' references unknown node: {edge['from']}")
            if 'to' in edge and edge['to'] not in node_ids:
                self.error(f"Edge {i}: 'to' references unknown node: {edge['to']}")

    def validate_gates(self):
        """Validate gate references"""
        if 'gates' not in self.fg:
            self.warning("No gates defined")
            return

        gates_dir = self.repo_root / 'freedomation' / 'gates'

        for i, gate in enumerate(self.fg['gates']):
            # Check required fields
            required = ['gate_id', 'position', 'gate_ref']
            for field in required:
                if field not in gate:
                    self.error(f"Gate {i}: missing required field '{field}'")

            # Check gate file exists
            if 'gate_ref' in gate:
                gate_ref = gate['gate_ref']
                gate_file = gates_dir / f"{gate_ref}.yaml"
                if not gate_file.exists():
                    self.error(f"Gate {i}: gate file not found: {gate_file}")

    def validate_outputs(self):
        """Validate outputs section"""
        if 'outputs' not in self.fg:
            self.error("Missing 'outputs' section")
            return

        if not isinstance(self.fg['outputs'], list):
            self.error("'outputs' should be a list")
            return

        if len(self.fg['outputs']) == 0:
            self.warning("No outputs defined")

    def error(self, msg):
        """Record an error"""
        self.errors.append(f"ERROR: {msg}")

    def warning(self, msg):
        """Record a warning"""
        self.warnings.append(f"WARNING: {msg}")

    def report(self):
        """Print validation report"""
        print()

        if self.warnings:
            print("WARNINGS:")
            for w in self.warnings:
                print(f"  {w}")
            print()

        if self.errors:
            print("ERRORS:")
            for e in self.errors:
                print(f"  {e}")
            print()
            print(f"❌ Validation FAILED ({len(self.errors)} errors, {len(self.warnings)} warnings)")
        else:
            print(f"✅ Validation PASSED ({len(self.warnings)} warnings)")

        print("-" * 60)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 flowgram_validate.py <flowgram.yaml>")
        sys.exit(1)

    flowgram_path = sys.argv[1]

    if not Path(flowgram_path).exists():
        print(f"ERROR: File not found: {flowgram_path}")
        sys.exit(1)

    validator = FlowgramValidator(flowgram_path)
    success = validator.validate()

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
