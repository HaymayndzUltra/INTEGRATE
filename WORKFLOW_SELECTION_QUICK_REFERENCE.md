# Quick Reference: Workflow Selection Guide

## 🚀 Quick Start

```bash
# Analyze your project brief
python enhanced_workflow_selector.py "Your project brief here"

# Interactive mode
python enhanced_workflow_selector.py --interactive

# Save results as JSON
python enhanced_workflow_selector.py "Your brief" --json
```

## 📋 What to Include in Your Project Brief

### Essential Information:

1. **Core Features Needed**
   - Knowledge management
   - Task tracking
   - RAG/search capabilities
   - Agent development
   - Web crawling
   - etc.

2. **Technical Stack**
   - Programming languages (Python, TypeScript, etc.)
   - Frameworks (React, FastAPI, etc.)
   - Infrastructure (Supabase, Neo4j, etc.)

3. **Project Characteristics**
   - New project vs existing project
   - Solo developer vs team
   - Simple vs complex requirements

4. **Priority Requirements**
   - What's critical vs nice-to-have
   - Timeline constraints
   - Team size and expertise

## 🎯 Workflow Quick Matcher

### Match by Primary Need:

**Knowledge Management + Task Tracking**
→ **Archon-main** (90%+ match)

**New Project + Structured Development**
→ **context-engineering-intro-main** (80%+ match)

**Web Crawling + RAG + Knowledge Graph**
→ **mcp-crawl4ai-rag-main** (95%+ match)

**Specialized Agent Development**
→ **ottomator-agents-main** (90%+ match)

**Protocol-Based + Template Generation**
→ **SuperTemplate-master** (95%+ match)

## 💡 Decision Flow

```
Start: What's your primary need?
│
├─ Knowledge Management?
│  └─ YES → Archon-main
│
├─ Starting New Project?
│  └─ YES → context-engineering-intro-main
│
├─ Web Crawling + RAG?
│  └─ YES → mcp-crawl4ai-rag-main
│
├─ Building Agents?
│  └─ YES → ottomator-agents-main
│
└─ Need Protocols/Validation?
   └─ YES → SuperTemplate-master
```

## 📊 Score Interpretation

- **90-100%**: Perfect match, highly recommended
- **70-89%**: Strong match, good fit
- **60-69%**: Suitable match, consider alternatives
- **40-59%**: Partial match, may need adaptation
- **<40%**: Poor match, consider other workflows

## 🔄 Combining Workflows

You can combine workflows:
- Use **Archon** for knowledge management
- Use **mcp-crawl4ai-rag** for advanced RAG
- Extract patterns from **ottomator-agents**
- Use **SuperTemplate** for governance

## ⚠️ Common Mistakes

1. **Too Vague**: "Build an app" → Be specific
2. **Ignoring Scale**: Solo vs team matters
3. **Tech Stack Mismatch**: Check compatibility
4. **Over-Engineering**: Simple needs → simple workflow

## 📞 Getting Help

1. Check workflow-specific README files
2. Review session analysis reports
3. Consult `WORKFLOW_SELECTION_FRAMEWORK.md`
4. Run enhanced selector with your brief

---

**Last Updated**: 2025-11-02

