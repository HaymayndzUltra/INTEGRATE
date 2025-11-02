# INTEGRATE

A comprehensive workspace for AI workflow development, analysis, and integration. This repository contains five core AI workflow systems alongside an advanced rule-based governance framework for systematic workflow analysis and improvement.

## 🎯 Purpose

INTEGRATE serves as a unified workspace for:
- **Workflow Analysis**: Systematic, iterative analysis of AI workflow implementations
- **Pattern Integration**: Cross-pollination of best practices across workflows
- **Governance Framework**: Rule-based system for consistent AI-assisted development
- **Context Engineering**: Structured approach to providing context to AI coding assistants

## 📁 Project Structure

```
INTEGRATE/
├── Archon-main/              # Knowledge management & task tracking system
├── context-engineering-intro-main/  # Context Engineering templates & PRP framework
├── mcp-crawl4ai-rag-main/    # Advanced RAG with crawling & knowledge graphs
├── ottomator-agents-main/    # Specialized AI agent implementations
├── SuperTemplate-master/     # Protocol-based workflow template system
├── .cursor/rules/           # AI governance rules (master-rules, common-rules)
├── session-suggestions/      # Iterative workflow analysis session reports
├── IMPROVED_PROMPT.md       # Workflow analysis protocol specification
└── README.md                 # This file
```

## 🏗️ Core Workflows

### 1. Archon-main
**Purpose**: Knowledge management and task tracking system for AI coding assistants

**Key Features**:
- MCP (Model Context Protocol) server integration
- Web crawling and document processing
- Advanced RAG strategies (contextual embeddings, hybrid search, reranking)
- Project and task management
- Real-time collaboration via WebSocket

**Tech Stack**: React, FastAPI, Supabase, PydanticAI

**Documentation**: `Archon-main/Archon-main/README.md`

---

### 2. context-engineering-intro-main
**Purpose**: Template and framework for Context Engineering methodology

**Key Features**:
- PRP (Product Requirements Prompt) framework
- CLAUDE.md rule system for project-specific AI guidance
- Multiple use cases (MCP server, PydanticAI agents, template generation)
- Example-driven development patterns

**Documentation**: `context-engineering-intro-main/context-engineering-intro-main/README.md`

---

### 3. mcp-crawl4ai-rag-main
**Purpose**: MCP server providing advanced web crawling and RAG capabilities

**Key Features**:
- Crawl4AI integration for smart web crawling
- Knowledge graph integration (Neo4j)
- AI hallucination detection
- Multiple RAG strategies (hybrid search, contextual embeddings, reranking)
- Repository code analysis

**Tech Stack**: Python, Crawl4AI, Supabase, Neo4j, Sentence Transformers

---

### 4. ottomator-agents-main
**Purpose**: Collection of specialized AI agent implementations

**Key Features**:
- Multiple agent patterns (RAG, knowledge graph, foundational)
- Airtable integration agents
- GitHub integration agents
- Slack integration agents
- Docling-based document processing

**Documentation**: Individual README files in each agent subdirectory

---

### 5. SuperTemplate-master
**Purpose**: Protocol-based workflow template system

**Key Features**:
- Structured workflow protocols
- Template generation system
- API design patterns

**Documentation**: `SuperTemplate-master/README.md` (if available)

---

## 🎛️ Governance Framework

### Rule System Structure

The project uses a hierarchical rule system located in `.cursor/rules/`:

```
.cursor/rules/
├── master-rules/          # Global framework governance
│   ├── context-discovery.mdc
│   ├── ai-collaboration-guidelines.mdc
│   ├── code-quality-checklist.mdc
│   ├── documentation-and-context-guidelines.mdc
│   ├── how-to-create-effective-rules.mdc
│   └── integrate-workflow-analysis.mdc
└── common-rules/          # Shared technical patterns (if any)
```

### Rule Types

1. **Master Rules** (`master-rules/`): Global framework governance
   - Workflow protocols
   - Meta-rules and quality standards
   - AI collaboration guidelines

2. **Common Rules** (`common-rules/`): Shared technical patterns
   - Cross-project conventions
   - API standards
   - Testing patterns

3. **Project Rules** (`{project}/.cursor/rules/project-rules/`): Project-specific rules
   - Feature-specific guidelines
   - Domain-specific patterns

### Rule Discovery

Rules are automatically discovered using metadata tags:
- **TAGS**: Domain classification (e.g., `[backend,api,testing]`)
- **TRIGGERS**: Keywords that activate the rule (e.g., `test,vitest,mock`)
- **SCOPE**: Applicability scope (e.g., `My-Node-Service`, `global`)
- **DESCRIPTION**: One-sentence summary

See `.cursor/rules/master-rules/6-master-rule-how-to-create-effective-rules.mdc` for creating new rules.

---

## 📊 Workflow Analysis System

### Session-Based Analysis

The project uses an iterative, session-based approach to analyze workflows:

1. **Location**: `session-suggestions/`
2. **Format**: `session-XX.md` (zero-padded session numbers)
3. **Principle**: "MERON LANG hindi puwede magdagdag kahit wala naman na"
   - Only add suggestions if genuine gaps exist
   - Build upon previous session findings
   - Avoid redundant suggestions

### Session Protocol

Each session:
1. **Discovers** previous session files
2. **Integrates** approved suggestions from prior sessions
3. **Analyzes** all five workflow directories
4. **Identifies** only NEW gaps (not previously documented)
5. **Documents** findings with evidence (file paths, line numbers)

### Running Analysis

The analysis protocol is defined in:
- `IMPROVED_PROMPT.md`: Detailed protocol specification
- `.cursor/rules/master-rules/integrate-workflow-analysis.mdc`: Rule-based protocol

**Current Sessions**: `session-01.md` through `session-04.md` (see `session-suggestions/` directory)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.12+ (for Python-based workflows)
- Node.js 18+ (for frontend workflows)
- Docker (optional, for containerized services)
- Git

### Initial Setup

1. **Clone or navigate to workspace**:
   ```bash
   cd /home/haymayndz/INTEGRATE
   ```

2. **Review workflow-specific READMEs**:
   - Each workflow directory contains its own `README.md` with setup instructions
   - Start with the workflow you're most interested in

3. **Understand the rule system**:
   - Read `.cursor/rules/master-rules/6-master-rule-how-to-create-effective-rules.mdc`
   - Review existing master rules to understand the governance framework

4. **Review analysis sessions**:
   - Check `session-suggestions/session-01.md` for initial findings
   - Review latest session for current recommendations

### Working with a Specific Workflow

1. **Archon**: See `Archon-main/Archon-main/README.md` for setup
2. **Context Engineering**: See `context-engineering-intro-main/context-engineering-intro-main/README.md`
3. **Crawl4AI RAG**: Check workflow-specific README files
4. **Ottomator Agents**: Review individual agent READMEs
5. **SuperTemplate**: See template documentation

---

## 📝 Documentation Standards

### Documentation Updates

Per `.cursor/rules/master-rules/5-master-rule-documentation-and-context-guidelines.mdc`:

- **[STRICT]** Documentation MUST be updated after significant code changes
- **[STRICT]** Security changes require immediate documentation updates
- **[GUIDELINE]** Follow established documentation patterns within each workflow

### Documentation Structure

Each workflow should maintain:
- `README.md`: Overview, quick start, architecture
- `docs/`: Detailed documentation (if applicable)
- `.env.example`: Environment variable templates
- `CONTRIBUTING.md`: Contribution guidelines (if applicable)

---

## 🔍 Current Analysis Status

**Latest Session**: `session-04.md` (2025-11-02)

### Key Findings Across Workflows

**Common Strengths**:
- Well-structured codebases with clear separation of concerns
- Modern tech stacks and dependency management
- Comprehensive feature sets

**Common Gaps Identified**:
- **CI/CD**: No standardized GitHub Actions workflows across workflows
- **Configuration**: Missing `.env.example` files in some workflows
- **Testing**: Inconsistent test coverage and frameworks
- **Documentation**: Some workflows lack comprehensive API documentation

**Integration Opportunities**:
- Shared logging utilities (Archon's structured logger)
- Unified CI/CD templates
- Standardized configuration patterns
- Cross-workflow pattern sharing

See `session-suggestions/session-04.md` for detailed analysis.

---

## 🤝 Contributing

### Adding New Workflows

1. Create workflow directory in root
2. Add workflow-specific README
3. Include `.env.example` if configuration is needed
4. Add workflow to this README's "Core Workflows" section

### Creating Rules

1. Review `.cursor/rules/master-rules/6-master-rule-how-to-create-effective-rules.mdc`
2. Classify rule type (master/common/project)
3. Follow 4 Pillars structure:
   - Structure & Discoverability
   - Personality & Intent
   - Precision & Clarity
   - Exemplarity & Contrast
4. Use proper metadata format

### Running Workflow Analysis

Follow the protocol in `IMPROVED_PROMPT.md`:
1. Discover previous sessions
2. Integrate approved suggestions
3. Analyze five workflows systematically
4. Document only NEW gaps with evidence
5. Create next session file

---

## 📚 Additional Resources

- **Archon Documentation**: `Archon-main/Archon-main/docs/`
- **Context Engineering Guide**: `context-engineering-intro-main/context-engineering-intro-main/README.md`
- **Rule Creation Guide**: `.cursor/rules/master-rules/6-master-rule-how-to-create-effective-rules.mdc`
- **Analysis Protocol**: `IMPROVED_PROMPT.md`

---

## 🏷️ License

Individual workflows may have their own licenses. Check each workflow's directory for license information.

---

## 📞 Support

For workflow-specific issues:
- **Archon**: See `Archon-main/Archon-main/README.md` for support links
- **Other workflows**: Check individual workflow READMEs

For INTEGRATE workspace issues:
- Review session suggestions in `session-suggestions/`
- Check rule documentation in `.cursor/rules/`

---

**Last Updated**: Based on session-04.md analysis (2025-11-02)
