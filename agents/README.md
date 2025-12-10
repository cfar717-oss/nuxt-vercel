# Agents Directory

This directory contains your **~30 agentic architecture** components, organized by pipeline type.

## Structure

### XML Pipeline (`xml/`)
Structured, formal agent definitions using XML schemas.

- **copywriting/** - Core copywriting agents (headlines, CTAs, body copy)
- **research/** - Research and analysis agents (audience, competitors, insights)
- **formatting/** - Output formatting agents (structure, styling, templates)

### Markdown Pipeline (`markdown/`)
Conversational, flexible agent definitions using Markdown.

- **conversational/** - Chat-style agents for iterative refinement
- **orchestration/** - Multi-agent workflow coordinators
- **docs/** - Documentation and knowledge base agents

### Shared (`shared/`)
Common utilities, helpers, and configurations used across both pipelines.

## Agent Architecture Pattern

Each agent should follow this structure:

### XML Agent Example
```xml
<!-- agents/xml/copywriting/headline-generator.xml -->
<agent>
  <name>Headline Generator</name>
  <type>copywriting</type>
  <purpose>Creates authentic, benefit-driven headlines</purpose>
  <inputs>
    <input name="product" required="true" />
    <input name="audience" required="true" />
    <input name="benefit" required="true" />
    <input name="emotion" required="false" />
  </inputs>
  <outputs>
    <output type="variants" count="3" />
    <output type="recommendation" />
    <output type="reasoning" />
  </outputs>
  <prompt>
    <![CDATA[
      Generate an authentic, benefit-driven headline for {{product}}.

      Context:
      - Target audience: {{audience}}
      - Core benefit: {{benefit}}
      - Emotional driver: {{emotion}}

      Create 3 headline variants...
    ]]>
  </prompt>
</agent>
```

### Markdown Agent Example
```markdown
<!-- agents/markdown/copywriting/headline-generator.md -->
# Headline Generator Agent

**Type:** Copywriting
**Purpose:** Creates authentic, benefit-driven headlines

## Inputs
- `product` (required): Product/service name
- `audience` (required): Target audience description
- `benefit` (required): Core benefit to highlight
- `emotion` (optional): Emotional driver

## Outputs
1. Three headline variants
2. Recommended choice
3. Reasoning for recommendation

## Prompt Template
\`\`\`
Generate an authentic, benefit-driven headline for {{product}}.

Context:
- Target audience: {{audience}}
- Core benefit: {{benefit}}
- Emotional driver: {{emotion}}

Create 3 headline variants:
1. Curiosity-driven
2. Benefit-focused
3. Narrative-driven

Then recommend the best choice with reasoning.
\`\`\`
```

## Migration from Chat to Claude Code

### Step 1: Document Your Chat Agent
1. Copy the prompt you use in Claude chat
2. Identify inputs (what variables you provide)
3. Define outputs (what you expect back)

### Step 2: Choose Your Pipeline
- **XML:** For structured, formal, reusable agents
- **Markdown:** For flexible, conversational agents

### Step 3: Create Agent File
- Use the patterns above as templates
- Save in appropriate directory

### Step 4: Test & Iterate
- Test agent via slash command
- Refine prompt and structure
- Document learnings

## Progressive Disclosure

Start with your **top 5 most-used agents**, then expand:

1. ✅ Headline Generator
2. ✅ CTA Creator
3. ✅ Sales Page Outline
4. ✅ Email Sequence Planner
5. ✅ Proof Element Generator

Then add the rest of your 30 agents progressively.

## Self-Healing Patterns

Agents should include:
- **Error handling:** What to do when inputs are unclear
- **Fallback options:** Alternative approaches if first attempt fails
- **Validation:** Check outputs before returning
- **Recovery:** How to restart or retry

## Next Steps

1. Start migrating your most-used agent
2. Test it as a slash command
3. Refine based on results
4. Repeat for remaining agents

See `/workflows` for multi-agent orchestration patterns.
