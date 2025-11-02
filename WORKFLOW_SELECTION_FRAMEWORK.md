# Workflow Selection Framework
# Intelligent Workflow Recommendation System Based on Project Brief

## 🎯 Purpose

This framework analyzes project briefs and recommends the most appropriate workflow from the INTEGRATE ecosystem. The enhanced system uses multi-dimensional scoring, decision matrix analysis, and intelligent pattern matching to provide accurate workflow recommendations.

**Key Features:**
- ✅ Multi-dimensional requirement analysis
- ✅ Intelligent pattern matching
- ✅ Weighted scoring system
- ✅ Detailed match explanations
- ✅ Consideration of project type and scale
- ✅ Tech stack compatibility checking

## 📋 Decision Framework

### Step 1: Analyze Project Brief

Extract key information from project brief:

1. **Project Type**
   - New project vs Existing project
   - Feature addition vs Complete rewrite
   - Research/exploration vs Production system

2. **Primary Requirements**
   - Knowledge management needs
   - RAG/search capabilities
   - Agent functionality
   - Documentation needs
   - Task management

3. **Technical Constraints**
   - Programming language (Python, TypeScript, etc.)
   - Infrastructure (Supabase, Neo4j, etc.)
   - Integration requirements (MCP, APIs, etc.)

4. **Team/Scale**
   - Solo developer vs Team
   - Small project vs Enterprise
   - Rapid prototyping vs Long-term maintenance

---

## 🔍 Workflow Selection Matrix

### Workflow 1: Archon-main
**Best For:**
- ✅ Knowledge management & documentation systems
- ✅ Projects requiring task tracking and project management
- ✅ Teams needing centralized knowledge base
- ✅ Multi-agent AI coding workflows
- ✅ Real-time collaboration features
- ✅ Complex web applications (React + FastAPI)

**Project Brief Indicators:**
- "Need to manage documentation"
- "Track tasks and projects"
- "Knowledge base for AI assistants"
- "Multi-service architecture"
- "Real-time updates"
- "MCP server integration"

**Tech Stack Match:**
- Python 3.12+
- React/TypeScript
- Supabase
- FastAPI

**When NOT to use:**
- ❌ Simple single-file scripts
- ❌ Pure backend APIs without UI
- ❌ Projects without knowledge management needs

---

### Workflow 2: context-engineering-intro-main
**Best For:**
- ✅ New projects starting from scratch
- ✅ Context Engineering methodology adoption
- ✅ PRP (Product Requirements Prompt) workflow
- ✅ Template-based development
- ✅ Learning Context Engineering patterns
- ✅ Structured feature development

**Project Brief Indicators:**
- "Starting new project"
- "Need structured development process"
- "Want to use PRP framework"
- "Template-based approach"
- "Context Engineering methodology"
- "Feature planning and execution"

**Tech Stack Match:**
- Python projects
- Pydantic AI agents
- MCP servers
- Cloudflare Workers

**When NOT to use:**
- ❌ Existing large codebases (use Archon instead)
- ❌ Simple scripts without structure needs
- ❌ Projects already using different methodology

---

### Workflow 3: mcp-crawl4ai-rag-main
**Best For:**
- ✅ Web crawling and scraping projects
- ✅ Advanced RAG implementations
- ✅ Knowledge graph integration
- ✅ AI hallucination detection
- ✅ Repository code analysis
- ✅ MCP server development

**Project Brief Indicators:**
- "Web crawling"
- "Document processing"
- "Knowledge graphs"
- "RAG search"
- "Code analysis"
- "Hallucination detection"
- "Neo4j integration"

**Tech Stack Match:**
- Python
- Crawl4AI
- Supabase
- Neo4j
- Sentence Transformers

**When NOT to use:**
- ❌ Projects without RAG needs
- ❌ Simple CRUD applications
- ❌ Projects without web crawling requirements

---

### Workflow 4: ottomator-agents-main
**Best For:**
- ✅ Specialized agent implementations
- ✅ Integration with external services (Airtable, GitHub, Slack)
- ✅ RAG agent patterns
- ✅ Document processing agents
- ✅ Multi-agent systems
- ✅ Agent-specific use cases

**Project Brief Indicators:**
- "AI agent"
- "Integration with [service]"
- "Specialized functionality"
- "Agent patterns"
- "RAG agent"
- "Document processing agent"
- "Airtable/GitHub/Slack integration"

**Tech Stack Match:**
- Python
- Pydantic AI
- Various integrations (Airtable, GitHub, Slack)
- Docling

**When NOT to use:**
- ❌ Full-stack applications
- ❌ Complex multi-service systems
- ❌ Projects requiring task management

---

### Workflow 5: SuperTemplate-master
**Best For:**
- ✅ Protocol-based development
- ✅ Template generation
- ✅ Structured workflow protocols
- ✅ Validation systems
- ✅ Artifact generation
- ✅ Quality gates

**Project Brief Indicators:**
- "Protocol-based"
- "Template generation"
- "Workflow protocols"
- "Validation system"
- "Quality gates"
- "Structured processes"

**Tech Stack Match:**
- Python
- Protocol systems
- Validation frameworks

**When NOT to use:**
- ❌ Simple one-off projects
- ❌ Projects not requiring protocols
- ❌ Rapid prototyping without structure

---

## 🤖 Enhanced Workflow Selector

### New Enhanced Selector (`enhanced_workflow_selector.py`)

The enhanced selector provides:

1. **Multi-Dimensional Analysis**
   - Core feature matching with weighted scores
   - Tech stack compatibility checking
   - Project type and scale considerations
   - Complexity and setup time matching

2. **Intelligent Pattern Matching**
   - Extracts keywords from project brief
   - Detects requirements using pattern matching
   - Identifies priority levels
   - Classifies project type and scale

3. **Weighted Scoring System**
   - Core requirements: 3.0x weight
   - Tech stack match: 2.0x weight
   - Project type match: 1.5x weight
   - Complexity/scale match: 1.0x weight

4. **Detailed Recommendations**
   - Match percentage (0-100%)
   - Score breakdown by category
   - Reasons for recommendation
   - Strengths and considerations
   - Alternative options

### Usage

**Command Line:**
```bash
python enhanced_workflow_selector.py "Build a knowledge management system with RAG search"
```

**Interactive Mode:**
```bash
python enhanced_workflow_selector.py --interactive
```

**JSON Output:**
```bash
python enhanced_workflow_selector.py "Your brief here" --json
```

### Algorithm: Project Brief Analysis → Workflow Recommendation

```python
def analyze_project_brief(brief: str) -> dict:
    """
    Analyze project brief and extract key indicators.
    
    Returns:
        Dictionary with extracted requirements and indicators
    """
    indicators = {
        'knowledge_management': False,
        'task_tracking': False,
        'web_crawling': False,
        'rag_search': False,
        'agent_development': False,
        'protocol_based': False,
        'new_project': False,
        'multi_service': False,
        'mcp_server': False,
        'knowledge_graph': False,
    }
    
    brief_lower = brief.lower()
    
    # Pattern matching
    if any(word in brief_lower for word in ['knowledge', 'documentation', 'docs']):
        indicators['knowledge_management'] = True
    
    if any(word in brief_lower for word in ['task', 'project management', 'tracking']):
        indicators['task_tracking'] = True
    
    if any(word in brief_lower for word in ['crawl', 'scrape', 'web']):
        indicators['web_crawling'] = True
    
    if any(word in brief_lower for word in ['rag', 'search', 'embedding', 'vector']):
        indicators['rag_search'] = True
    
    if any(word in brief_lower for word in ['agent', 'ai agent', 'pydantic ai']):
        indicators['agent_development'] = True
    
    if any(word in brief_lower for word in ['protocol', 'template', 'workflow']):
        indicators['protocol_based'] = True
    
    if any(word in brief_lower for word in ['new', 'start', 'begin', 'create']):
        indicators['new_project'] = True
    
    if any(word in brief_lower for word in ['multi', 'microservice', 'service']):
        indicators['multi_service'] = True
    
    if 'mcp' in brief_lower or 'model context protocol' in brief_lower:
        indicators['mcp_server'] = True
    
    if any(word in brief_lower for word in ['knowledge graph', 'neo4j', 'graph']):
        indicators['knowledge_graph'] = True
    
    return indicators


def recommend_workflow(indicators: dict) -> list:
    """
    Recommend workflows based on indicators.
    
    Returns:
        List of recommended workflows ordered by relevance score
    """
    scores = {
        'Archon-main': 0,
        'context-engineering-intro-main': 0,
        'mcp-crawl4ai-rag-main': 0,
        'ottomator-agents-main': 0,
        'SuperTemplate-master': 0,
    }
    
    # Archon scoring
    if indicators['knowledge_management']:
        scores['Archon-main'] += 3
    if indicators['task_tracking']:
        scores['Archon-main'] += 3
    if indicators['multi_service']:
        scores['Archon-main'] += 2
    if indicators['mcp_server']:
        scores['Archon-main'] += 2
    if indicators['rag_search']:
        scores['Archon-main'] += 1
    
    # Context Engineering scoring
    if indicators['new_project']:
        scores['context-engineering-intro-main'] += 3
    if indicators['agent_development']:
        scores['context-engineering-intro-main'] += 2
    if indicators['protocol_based']:
        scores['context-engineering-intro-main'] += 1
    
    # Crawl4AI RAG scoring
    if indicators['web_crawling']:
        scores['mcp-crawl4ai-rag-main'] += 3
    if indicators['rag_search']:
        scores['mcp-crawl4ai-rag-main'] += 2
    if indicators['knowledge_graph']:
        scores['mcp-crawl4ai-rag-main'] += 3
    if indicators['mcp_server']:
        scores['mcp-crawl4ai-rag-main'] += 2
    
    # Ottomator Agents scoring
    if indicators['agent_development']:
        scores['ottomator-agents-main'] += 3
    if indicators['rag_search']:
        scores['ottomator-agents-main'] += 1
    
    # SuperTemplate scoring
    if indicators['protocol_based']:
        scores['SuperTemplate-master'] += 3
    if indicators['new_project']:
        scores['SuperTemplate-master'] += 1
    
    # Sort by score
    recommendations = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )
    
    return recommendations
```

---

## 📊 Decision Tree

```
Project Brief Analysis
│
├─ Need Knowledge Management + Task Tracking?
│  └─ YES → Archon-main
│
├─ New Project + Structured Development?
│  └─ YES → context-engineering-intro-main
│
├─ Web Crawling + RAG + Knowledge Graph?
│  └─ YES → mcp-crawl4ai-rag-main
│
├─ Specialized Agent Development?
│  └─ YES → ottomator-agents-main
│
└─ Protocol-Based + Template Generation?
   └─ YES → SuperTemplate-master
```

---

## 🎯 Example Scenarios

### Scenario 1: "Build a knowledge base system for our documentation"
**Analysis:**
- Knowledge management: ✅
- Task tracking: Maybe
- RAG search: ✅
- Multi-service: Maybe

**Recommendation:** **Archon-main** (90% match)
- Perfect for knowledge management
- Built-in RAG capabilities
- Task tracking available if needed

---

### Scenario 2: "Create a new AI agent for customer support"
**Analysis:**
- Agent development: ✅
- New project: ✅
- Structured process: ✅

**Recommendation:** **context-engineering-intro-main** (80% match)
- PRP framework for structured development
- Agent templates available
- Context Engineering methodology

**Alternative:** **ottomator-agents-main** (70% match) if specific agent patterns needed

---

### Scenario 3: "Build web crawler with RAG for code documentation"
**Analysis:**
- Web crawling: ✅
- RAG search: ✅
- Knowledge graph: Maybe

**Recommendation:** **mcp-crawl4ai-rag-main** (95% match)
- Built-in Crawl4AI integration
- Advanced RAG strategies
- Knowledge graph support available

---

### Scenario 4: "Need a GitHub integration agent"
**Analysis:**
- Agent development: ✅
- Specific integration: ✅

**Recommendation:** **ottomator-agents-main** (90% match)
- Has GitHub integration agents
- Specialized agent patterns
- Ready-to-use examples

---

### Scenario 5: "Create a protocol-based workflow system"
**Analysis:**
- Protocol-based: ✅
- Template generation: ✅
- Validation: ✅

**Recommendation:** **SuperTemplate-master** (95% match)
- Protocol system built-in
- Template generation
- Quality gates

---

## 🔧 Implementation Guide

### How to Use This Framework

1. **Extract Project Brief**
   - Read the project brief/requirements
   - Note key features and requirements

2. **Run Analysis**
   - Use the `analyze_project_brief()` function
   - Or manually check indicators

3. **Get Recommendations**
   - Use the `recommend_workflow()` function
   - Review scores and top recommendations

4. **Validate Choice**
   - Check workflow documentation
   - Verify tech stack compatibility
   - Consider team expertise

5. **Adapt as Needed**
   - Workflows can be combined
   - Extract specific patterns
   - Customize for your needs

---

## 🚀 Integration with RAG MCP Server

This framework can be enhanced with RAG capabilities:

1. **Vectorize Project Briefs**
   - Store historical project briefs
   - Create embeddings for semantic search

2. **Similarity Matching**
   - Find similar past projects
   - Recommend workflows that worked before

3. **Continuous Learning**
   - Track workflow success rates
   - Improve recommendations over time

4. **Knowledge Base Integration**
   - Use Archon to store project briefs
   - Enable RAG search across briefs
   - Recommend workflows based on similar projects

---

## 📝 Usage Examples

### Example 1: Command-Line Tool

```bash
python workflow_selector.py --brief "Build a knowledge management system for documentation"
```

**Output:**
```
Analyzing project brief...
Key indicators detected:
- knowledge_management: True
- rag_search: True
- task_tracking: True

Recommendations:
1. Archon-main (Score: 9/10)
   - Perfect match for knowledge management
   - Built-in RAG capabilities
   - Task tracking available

2. mcp-crawl4ai-rag-main (Score: 6/10)
   - Good RAG capabilities
   - Missing task management

3. context-engineering-intro-main (Score: 4/10)
   - Template-based approach
   - Less suitable for existing systems
```

### Example 2: API Integration

```python
from workflow_selector import analyze_project_brief, recommend_workflow

brief = """
We need to build a system that:
- Crawls documentation websites
- Stores content in a knowledge base
- Provides RAG search capabilities
- Tracks documentation projects
"""

indicators = analyze_project_brief(brief)
recommendations = recommend_workflow(indicators)

print(f"Top recommendation: {recommendations[0][0]}")
```

---

## 🎓 Best Practices

1. **Combine Workflows**
   - Use Archon for knowledge management
   - Use mcp-crawl4ai-rag for advanced RAG
   - Extract patterns from ottomator-agents

2. **Start Simple**
   - Begin with one primary workflow
   - Add complexity as needed
   - Extract patterns rather than full adoption

3. **Validate Before Committing**
   - Check workflow documentation
   - Verify tech stack compatibility
   - Consider team learning curve

4. **Iterate**
   - Start with recommendations
   - Adjust based on experience
   - Document what works

---

## 🎓 How to Use This Framework

### Step-by-Step Process

1. **Write Your Project Brief**
   - Be specific about requirements
   - Mention key features needed
   - Include technical constraints
   - Specify project type and scale

2. **Run the Enhanced Selector**
   ```bash
   python enhanced_workflow_selector.py "Your project brief here"
   ```

3. **Review Recommendations**
   - Check match percentage (aim for 60%+)
   - Read detailed score breakdown
   - Review strengths and considerations
   - Consider alternative workflows

4. **Validate Your Choice**
   - Review workflow documentation
   - Verify tech stack compatibility
   - Check team expertise
   - Consider learning curve

5. **Start Implementation**
   - Follow workflow setup instructions
   - Adapt patterns to your needs
   - Combine workflows if needed

### Best Practices

**✅ Good Project Brief Examples:**

```
"Build a knowledge management system for our documentation with RAG search capabilities. 
Need task tracking and project management. Team of 5 developers. Using Python and React."
```

```
"Starting a new AI agent project. Need structured development process with PRP framework. 
Solo developer. Python-based."
```

**❌ Vague Project Briefs:**

```
"Build something cool"
```

```
"Make an app"
```

### Decision Matrix Quick Reference

| Requirement | Archon | Context Eng | Crawl4AI | Ottomator | SuperTemplate |
|------------|--------|-------------|----------|-----------|---------------|
| Knowledge Mgmt | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| Task Tracking | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐ | ⭐ | ⭐ |
| Web Crawling | ⭐⭐⭐ | ⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐ |
| RAG Search | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐ |
| Agent Dev | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| MCP Server | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| Multi-Service | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐ | ⭐ |
| Protocol-Based | ⭐⭐ | ⭐⭐⭐ | ⭐ | ⭐ | ⭐⭐⭐⭐⭐ |

## 📚 References

- [RAG MCP Server Video](https://www.youtube.com/watch?v=ZoyPqXvnnZ8)
- Archon Documentation: `Archon-main/Archon-main/README.md`
- Context Engineering: `context-engineering-intro-main/context-engineering-intro-main/README.md`

---

**Last Updated**: 2025-11-02
**Version**: 2.0 (Enhanced with multi-dimensional analysis)

