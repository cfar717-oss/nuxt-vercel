# Claude Code: Agentic Architecture Constitution

> **System Designer:** Non-dev founder/project builder focused on copywriting, sales systems, and agentic workflows
> **Last Updated:** 2025-12-10
> **Version:** 1.0.0

---

## 🎯 System Philosophy

This repository houses a **super-skill agentic architecture** designed for:
- Next-generation, authentic copywriting
- Long-form sales pages & sales letters (SLs)
- Advertorials, ads, and email sequences
- Video scripts and narrative-driven selling

### Core Principles

1. **System-First Thinking:** Architecture drives implementation
2. **Dual Pipeline Approach:** Both XML and Markdown representations
3. **Progressive Disclosure:** Information revealed as needed
4. **Self-Healing Systems:** Agents that can recover and adapt
5. **Non-Dev Friendly:** Tools amplify human creativity, not replace it

---

## 🏗️ Architecture Overview

### Agent Ecosystem (~30 Agents)

```
Agentic Super-Skill Architecture
├── XML Pipeline (agents/xml/)
│   ├── Core copywriting agents
│   ├── Research & analysis agents
│   └── Output formatting agents
├── Markdown Pipeline (agents/markdown/)
│   ├── Conversational agents
│   ├── Workflow orchestration
│   └── Documentation agents
└── Integration Layer
    ├── Heptabase (visual mapping)
    ├── V0 (UI prototyping)
    └── Vercel (deployment)
```

---

## 📁 Project Structure

```
nuxt-vercel/
├── CLAUDE.md                    # This file - system constitution
├── .claude/                     # Claude Code configuration
│   ├── commands/                # Slash commands (agent shortcuts)
│   ├── skills/                  # Packaged agentic capabilities
│   └── hooks/                   # Automation triggers
├── agents/                      # Agentic architecture
│   ├── xml/                     # XML-based agents
│   │   ├── copywriting/         # Core copy agents
│   │   ├── research/            # Research agents
│   │   └── formatting/          # Output agents
│   ├── markdown/                # Markdown-based agents
│   │   ├── conversational/      # Chat-style agents
│   │   ├── orchestration/       # Workflow agents
│   │   └── docs/                # Documentation agents
│   └── shared/                  # Shared utilities
├── workflows/                   # Multi-agent workflows
│   ├── sales-page/              # Sales page generation
│   ├── email-sequence/          # Email sequence creation
│   └── video-script/            # Video script development
├── templates/                   # Reusable templates
│   ├── prompts/                 # Prompt templates
│   ├── structures/              # Document structures
│   └── styles/                  # Style guides
└── integrations/                # External integrations
    ├── heptabase/               # Visual mapping
    ├── v0/                      # UI components
    └── vercel/                  # Deployment configs
```

---

## 🤖 Working With This System

### For Claude Code (You're Reading This!)

When working in this repository:

1. **Respect the dual pipeline:** Always maintain both XML and Markdown versions
2. **Progressive disclosure:** Don't overwhelm with all agents at once
3. **Self-healing priority:** Build in error recovery and adaptation
4. **Non-dev context:** Explain technical concepts in system-design language
5. **Copywriting focus:** Understand this is about authentic, effective copy

### Language & Communication

- **Prefer:** System design terminology, workflow language, copywriting concepts
- **Avoid:** Heavy technical jargon, low-level implementation details
- **When coding:** Explain *why* and *how it fits the system*, not just *what*

### Code Style & Patterns

```typescript
// Prefer: Clear, documented, system-oriented code
export interface AgentConfig {
  name: string           // Human-readable agent name
  type: 'xml' | 'md'     // Pipeline type
  purpose: string        // What this agent does
  triggers: string[]     // When to invoke
}

// Good: Self-documenting with clear purpose
const copywritingAgent: AgentConfig = {
  name: 'Headline Generator',
  type: 'md',
  purpose: 'Creates authentic, benefit-driven headlines',
  triggers: ['sales-page', 'advertorial', 'email-subject']
}
```

---

## 🎨 Copywriting System Conventions

### Voice & Tone Guidelines

- **Authentic over clever:** Real benefits beat wordplay
- **Narrative-driven:** Stories sell better than features
- **Benefit-focused:** Always answer "What's in it for me?"
- **Emotional connection:** Logic justifies, emotion decides

### Content Structure Patterns

1. **Sales Pages:**
   - Hook → Problem → Agitation → Solution → Proof → Offer → CTA

2. **Email Sequences:**
   - Awareness → Interest → Desire → Action (AIDA)

3. **Video Scripts:**
   - Pattern interrupt → Story → Transformation → Next step

---

## 🔧 Development Workflow

### 1. Chat-Based Design Phase
- Design agents in consumer Claude chat
- Iterate on prompts and behaviors
- Document in markdown/XML

### 2. Migration to Claude Code
- Convert chat agents to slash commands
- Package as skills
- Add automation via hooks

### 3. Integration & Deployment
- Connect to Heptabase for visual mapping
- Use V0 for UI components
- Deploy via Vercel

### 4. Iteration & Evolution
- Monitor agent performance
- Refine prompts and workflows
- Expand agent ecosystem

---

## 📊 Agent Development Pattern

### Converting Chat Agents → Claude Code Skills

**Before (Chat-based):**
```
User: "Generate a headline for a sales page about [product]"
Claude: [generates headline]
User: "Now make it more benefit-focused"
Claude: [refines headline]
```

**After (Claude Code Skill):**
```bash
# .claude/commands/headline.md
Generate an authentic, benefit-driven headline for {{product}}.

Context:
- Target audience: {{audience}}
- Core benefit: {{benefit}}
- Emotional driver: {{emotion}}

Output:
1. Initial headline (curiosity-driven)
2. Benefit-focused variant
3. Narrative-driven variant
4. Recommended choice with reasoning
```

Usage: `/headline product="Course Name" benefit="Save time" emotion="relief"`

---

## 🔗 Integration Specifications

### Heptabase Integration
- Export agent relationships as graph nodes
- Link prompts to architecture docs
- Visualize workflow dependencies
- Track system evolution over time

### V0 Integration
- Generate UI for sales pages
- Rapid prototype landing pages
- Component library for copy patterns
- A/B testing interfaces

### Vercel Deployment
- Auto-deploy on commit
- Preview branches for iterations
- Environment variables for API keys
- Analytics integration

---

## 🚀 Quick Start Commands

### Essential Slash Commands

```bash
/sales-page     # Generate complete sales page
/email-seq      # Create email sequence
/video-script   # Develop video script
/headline       # Generate headlines
/cta            # Create CTAs
/proof          # Generate proof elements
```

### Common Workflows

```bash
# Complete sales page workflow
/sales-page → /headline → /proof → /cta → deploy

# Email sequence workflow
/email-seq → review → refine → schedule

# Video script workflow
/video-script → /narrative → /cta → finalize
```

---

## 📚 Learning Resources

### For the System Designer (You!)

- **Prompt Engineering:** How to craft effective agent prompts
- **Workflow Design:** Orchestrating multi-agent systems
- **Integration Patterns:** Connecting tools into cohesive workflows

### For Claude Code (AI Assistant)

- **Copywriting Frameworks:** AIDA, PAS, Story frameworks
- **Sales Psychology:** What makes copy convert
- **Progressive Disclosure:** Revealing complexity gradually

---

## 🎯 Success Metrics

### Agent Performance
- Output quality (human evaluation)
- Iteration cycles to final copy
- Consistency across variants

### System Performance
- Agent reusability across projects
- Time saved vs. manual copywriting
- Self-healing instances

### Business Impact
- Conversion rate improvements
- Revenue attribution
- Client satisfaction scores

---

## 🔮 Future Vision

### Phase 1: Foundation (Current)
- Migrate 30 agents from chat to Claude Code
- Establish dual XML/MD pipelines
- Create core slash commands

### Phase 2: Integration
- Full Heptabase visual mapping
- V0 component library
- Automated deployment pipeline

### Phase 3: Evolution
- Self-healing agent systems
- AI-powered optimization
- Multi-client orchestration

### Phase 4: Scale
- Template marketplace
- Community agent sharing
- Enterprise deployment

---

## 💡 Key Mantras

> "Tools amplify creativity, they don't replace it"

> "System design beats implementation details"

> "Authentic copy converts better than clever copy"

> "Build with agents, not just for them"

---

## 🆘 Need Help?

- **Technical questions:** Ask Claude Code directly
- **Copywriting strategy:** Consult the agent library
- **System design:** Reference this CLAUDE.md
- **Integration issues:** Check integrations/ directory

---

**Remember:** This is a living document. As the agentic architecture evolves, so should this constitution.
