#!/usr/bin/env python3
"""
KB Linter v0.1
Lints Knowledge Block markdown files for compliance with KB spec.
"""

import sys
import re
from pathlib import Path


class KBLinter:
    REQUIRED_HEADINGS = [
        'Purpose',
        'Inputs',
        'Outputs',
        'Process',
        'Examples',
        'Edge Cases & Warnings',
        'Quality Checks',
        'Related KBs',
    ]

    REQUIRED_METADATA = [
        'Version',
        'Status',
        'Layer',
        'Type',
        'Category',
        'Credibility',
        'Risk',
    ]

    def __init__(self, kb_path):
        self.kb_path = Path(kb_path)
        self.errors = []
        self.warnings = []

    def lint(self):
        """Run all lint checks"""
        try:
            with open(self.kb_path) as f:
                self.content = f.read()
        except Exception as e:
            self.error(f"Failed to read file: {e}")
            return False

        self.check_kb_id()
        self.check_metadata()
        self.check_headings()
        self.check_change_log()

        return len(self.errors) == 0

    def check_kb_id(self):
        """Ensure KB ID in title matches filename"""
        filename_id = self.kb_path.stem  # KB-001
        title_match = re.search(r'^#\s+(KB-\d+):', self.content, re.MULTILINE)

        if not title_match:
            self.error("Missing KB ID in title (expected format: # KB-###: Title)")
            return

        title_id = title_match.group(1)
        if title_id != filename_id:
            self.error(f"KB ID mismatch: filename={filename_id}, title={title_id}")

    def check_metadata(self):
        """Check for required metadata fields"""
        # Look for metadata in first 30 lines
        lines = self.content.split('\n')[:30]
        metadata_section = '\n'.join(lines)

        for field in self.REQUIRED_METADATA:
            # Match **Field:** or Field: patterns
            pattern = rf'\*\*{field}:\*\*|^{field}:'
            if not re.search(pattern, metadata_section, re.MULTILINE):
                self.error(f"Missing metadata field: {field}")

    def check_headings(self):
        """Check for required section headings"""
        for heading in self.REQUIRED_HEADINGS:
            # Match ## Heading (allowing for "Examples/Templates" variations)
            heading_escaped = re.escape(heading)
            # Allow slight variations (e.g., "Examples" or "Examples/Templates")
            if heading == 'Examples':
                pattern = r'^##\s+(Examples|Examples/Templates)'
            else:
                pattern = rf'^##\s+{heading_escaped}'

            if not re.search(pattern, self.content, re.MULTILINE):
                self.error(f"Missing required section: ## {heading}")

    def check_change_log(self):
        """Check for change log"""
        if '**Change Log:**' not in self.content and 'Change Log:' not in self.content:
            self.warning("Missing change log section")

    def error(self, msg):
        """Record an error"""
        self.errors.append(f"ERROR: {msg}")

    def warning(self, msg):
        """Record a warning"""
        self.warnings.append(f"WARNING: {msg}")


def main():
    # Find all KB files
    repo_root = Path(__file__).parent.parent.parent
    kbs_dir = repo_root / 'freedomation' / 'kbs'

    if not kbs_dir.exists():
        print(f"ERROR: KBs directory not found: {kbs_dir}")
        sys.exit(1)

    kb_files = sorted(kbs_dir.glob('KB-*.md'))

    if not kb_files:
        print(f"No KB files found in {kbs_dir}")
        sys.exit(0)

    print(f"Linting {len(kb_files)} KB files...")
    print("=" * 60)
    print()

    total_errors = 0
    total_warnings = 0
    failed_kbs = []

    for kb_file in kb_files:
        linter = KBLinter(kb_file)
        success = linter.lint()

        total_errors += len(linter.errors)
        total_warnings += len(linter.warnings)

        if not success:
            failed_kbs.append(kb_file.name)

        # Report per file
        status = "✅" if success else "❌"
        print(f"{status} {kb_file.name}")

        if linter.errors:
            for error in linter.errors:
                print(f"    {error}")

        if linter.warnings:
            for warning in linter.warnings:
                print(f"    {warning}")

        if linter.errors or linter.warnings:
            print()

    # Summary
    print("=" * 60)
    print(f"Total: {len(kb_files)} KBs, {total_errors} errors, {total_warnings} warnings")

    if failed_kbs:
        print(f"❌ FAILED: {len(failed_kbs)} KBs have errors")
        sys.exit(1)
    else:
        print(f"✅ PASSED: All KBs validated successfully")
        sys.exit(0)


if __name__ == '__main__':
    main()
