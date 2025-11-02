# Meta Prompt Creator for Comprehensive Workflow System Analysis

## Purpose

Generate AI prompts that guarantee comprehensive analysis of complex workflow systems by ensuring complete documentation, code patterns, and architectural context is always included in every interaction.

## Target Systems

This creator analyzes these INTEGRATE workflow systems:
- **Archon** - MCP server for AI knowledge management
- **Context Engineering Intro** - Template for context engineering  
- **MCP Crawl4AI RAG** - Web crawling and RAG MCP server
- **Ottomator Agents** - AI agent collection platform
- **SuperTemplate** - 23-protocol AI-driven workflow

---

## Section 1: System Selection & Context Gathering

### Step 1.1: Select Target System(s)

Check which systems to analyze:
- [ ] Archon (`/home/haymayndz/INTEGRATE/Archon-main`)
- [ ] Context Engineering (`/home/haymayndz/INTEGRATE/context-engineering-intro-main`)
- [ ] MCP Crawl4AI RAG (`/home/haymayndz/INTEGRATE/mcp-crawl4ai-rag-main`)
- [ ] Ottomator Agents (`/home/haymayndz/INTEGRATE/ottomator-agents-main`)
- [ ] SuperTemplate (`/home/haymayndz/INTEGRATE/SuperTemplate-master`)

**Analysis Type**:
- [ ] Single system deep-dive
- [ ] Multi-system comparison
- [ ] Integration opportunity analysis
- [ ] Cross-system pattern analysis

### Step 1.2: Gather Complete System Context

For each selected system, collect:

**Required Documentation**:
1. README.md (full text)
2. Architecture/design docs
3. API/Protocol specifications
4. Setup/installation guides
5. Configuration examples

**Directory Structure**:
```bash
tree -L 3 -I 'node_modules|__pycache__|.git|dist|build' [system-path]
```

**Key Code Samples**:
- Main entry points
- Configuration files
- Protocol/API definitions
- Integration examples
- Test patterns

### Step 1.3: Identify Analysis Focus

What aspects need analysis?
- [ ] Architecture & design patterns
- [ ] Integration capabilities
- [ ] Code quality & maintainability  
- [ ] Documentation completeness
- [ ] Cross-system compatibility
- [ ] Implementation gaps
- [ ] Performance & scalability
- [ ] Security & error handling

---

## Section 2: Meta Prompt Template

### Base Template for Single System Analysis

```markdown
# Workflow System Analysis: [SYSTEM NAME]

## AI Persona & Expertise

You are a **Workflow System Architect** specializing in:
- AI-driven development workflows
- Model Context Protocol (MCP) servers and integrations
- Knowledge management and RAG systems
- Multi-system orchestration and integration patterns
- Code quality and architectural analysis

Your analysis must be evidence-based, citing specific files, sections, and code patterns.

---

## Critical Directive: Complete Context Preservation

**[STRICT]** You are analyzing a complete workflow system. You MUST:

1. **Read ALL provided documentation before analysis**
   - README files
   - Architecture documents  
   - API/protocol specifications
   - Configuration examples
   - Code samples

2. **Reference specific evidence**
   - File paths (e.g., `python/src/server/main.py`)
   - Section headings (e.g., "## Architecture Overview")
   - Line numbers when applicable (e.g., `lines 45-67`)
   - Exact quotes from documentation/code

3. **Maintain full system context**
   - Never assume features not explicitly documented
   - Consider all provided components
   - Flag missing information as gaps, not assumptions
   - Note integration points and dependencies

4. **Provide actionable insights**
   - Every finding must include file/section reference
   - Every recommendation must be specific and implementable
   - Every gap must be clearly described with impact assessment

---

## SYSTEM CONTENT

### System Metadata

**System Name**: [e.g., "Archon MCP Knowledge Server"]
**Repository Path**: [full absolute path]
**System Type**: [MCP Server / Template System / Workflow Platform / Agent Collection]
**Version/Date**: [version or last updated date]
**Primary Purpose**: [one-sentence mission statement]
**Core Technologies**: [languages, frameworks, key dependencies]

### System Documentation

#### README.md
```
[PASTE COMPLETE README.MD - DO NOT SUMMARIZE]











```

#### Architecture Documentation
```
[PASTE ARCHITECTURE.MD OR EQUIVALENT - IF EXISTS]








```

#### API/Protocol Specifications
```
[PASTE API DOCS, PROTOCOL DEFINITIONS - IF EXIST]








```

### System Structure

```
[PASTE OUTPUT OF: tree -L 3 -I 'node_modules|__pycache__|.git']










```

**File Statistics**:
- Total files: [count]
- Code files: [count by extension]
- Documentation files: [count]
- Configuration files: [count]
- Test files: [count]

### Key Code Patterns

#### Main Entry Point
```python
# File: [path]
[PASTE CODE - 20-50 lines showing main initialization]
```

#### Configuration Pattern
```python
# File: [path]
[PASTE CONFIG EXAMPLE]
```

#### API/Protocol Definition
```python
# File: [path]
[PASTE PROTOCOL/API DEFINITION]
```

#### Integration Example
```python
# File: [path]
[PASTE INTEGRATION CODE]
```

---

## Analysis Framework

### Phase 1: Comprehension Validation

Before proceeding, confirm you have:
- [ ] Read complete README and understood system purpose
- [ ] Reviewed directory structure and identified key components
- [ ] Examined code samples and understood patterns
- [ ] Noted all integration points and dependencies
- [ ] Identified documentation gaps

**Confirmation Statement**: 
"I have reviewed [X files, Y lines of documentation, Z code samples]. The system's primary purpose is [restate in own words]. Key components include [list 3-5 major subsystems]."

### Phase 2: Structured Analysis

Analyze the system across these dimensions:

#### Dimension 1: Architecture & Design

**Evaluation Criteria**:
- [ ] Is the overall architecture clearly documented?
- [ ] Are component responsibilities well-defined?
- [ ] Are data flows and dependencies mapped?
- [ ] Are design patterns consistent and appropriate?
- [ ] Are extension points identified?

**Required Evidence**:
- Quote architecture description from documentation
- Reference specific files showing architectural patterns
- Cite configuration examples
- Note any architectural inconsistencies with file/line references

**Output Format**:
```markdown
**Architecture Assessment**: [Rating 1-10]

**Strengths**:
- [Strength 1] - Evidence: "[quote from file X]"
- [Strength 2] - Evidence: File Y demonstrates [pattern]

**Weaknesses**:
- [Gap 1] - File: [path], Issue: [description], Impact: [High/Med/Low]
- [Gap 2] - Missing: [component], Needed for: [purpose]

**Patterns Identified**:
- Pattern: [name], Files: [list], Quality: [assessment]
```

#### Dimension 2: Implementation Quality

**Evaluation Criteria**:
- [ ] Is code organization logical and maintainable?
- [ ] Are dependencies properly managed?
- [ ] Is error handling comprehensive?
- [ ] Are testing strategies adequate?
- [ ] Is performance considered?

**Required Evidence**:
- Cite specific code files showing patterns
- Reference dependency management files
- Quote error handling examples
- Note test coverage (if documented)

#### Dimension 3: Integration & Interoperability

**Evaluation Criteria**:
- [ ] Are integration points clearly defined?
- [ ] Are protocols/APIs well-documented?
- [ ] Can this system compose with others?
- [ ] Are data formats standardized?
- [ ] Are integration examples provided?

**Required Evidence**:
- Quote API/protocol definitions
- Reference integration examples
- Cite configuration for external systems
- Note compatibility considerations

#### Dimension 4: Documentation & Usability

**Evaluation Criteria**:
- [ ] Is installation/setup clearly documented?
- [ ] Are usage examples comprehensive?
- [ ] Is troubleshooting guidance provided?
- [ ] Are all features documented?
- [ ] Can a new user successfully deploy?

**Required Evidence**:
- Reference setup instructions
- Quote usage examples
- Note documentation gaps with specific missing topics
- Cite troubleshooting sections (or note absence)

### Phase 3: Evidence-Based Findings

For every finding, provide:

**Finding Template**:
```markdown
**Finding**: [Clear title]
**Category**: [Architecture/Implementation/Integration/Documentation]
**Severity**: [Critical/High/Medium/Low]
**Evidence**: 
  - File: `[path]`
  - Section: "[heading or description]"
  - Line: [number or range]
  - Quote: "[exact text]"
**Analysis**: [What this means and why it matters]
**Impact**: [How this affects users/developers/integrations]
**Recommendation**: [Specific, actionable steps to address]
```

---

## Output Format Specification

Structure your response as follows:

### Part 1: Executive Summary (2-3 paragraphs)

- System purpose and scope
- Overall quality assessment (score with justification)
- Top 3 strengths with evidence
- Top 3 gaps/improvements with evidence
- Overall recommendation (Production Ready / Needs Work / Major Gaps)

### Part 2: Detailed Analysis by Dimension

For each dimension (Architecture, Implementation, Integration, Documentation):

```markdown
## Dimension: [Name]

### Score: [X/10]
**Calculation**: [Show breakdown, e.g., "Documentation: 2/2, Patterns: 3/4, Completeness: 3/4"]

### Strengths
1. **[Strength]**
   - Evidence: File `X`, lines Y-Z: "[quote]"
   - Impact: [Why this is good]

### Weaknesses
1. **[Gap]**
   - Evidence: File `X` missing [component]
   - Impact: [Why this matters]
   - Recommendation: [How to fix]

### Key Patterns
- Pattern: [name]
  - Files: [list]
  - Quality: [assessment with evidence]
```

### Part 3: Integration Analysis

```markdown
## Integration Capabilities

### Systems This Can Integrate With
- System: [name]
  - Integration Points: [APIs, protocols]
  - Evidence: File `X`, "[quote]"
  - Ease: [Easy/Moderate/Complex]

### Integration Gaps
- Missing: [capability]
  - Needed For: [use case]
  - Impact: [who this affects]
  - Recommendation: [how to add]
```

### Part 4: Actionable Recommendations

```markdown
## Prioritized Recommendations

### Critical (Must Fix)
1. **[Issue]**
   - Current State: File `X`, "[quote/description]"
   - Required Change: [specific action]
   - Impact: [benefit of fixing]
   - Effort: [S/M/L/XL]

### High Priority (Should Fix)
[Same format]

### Medium Priority (Nice to Have)
[Same format]

### Low Priority (Future Enhancement)
[Same format]
```

### Part 5: System Scorecard

```markdown
## Final Scorecard

| Dimension | Score | Evidence Summary |
|-----------|-------|------------------|
| Architecture | X/10 | [Key file refs] |
| Implementation | X/10 | [Key patterns] |
| Integration | X/10 | [Key capabilities] |
| Documentation | X/10 | [Completeness assessment] |
| **Overall** | **X/10** | **[Weighted average]** |

**Production Readiness**: [Ready / Needs Fixes / Not Ready]
**Recommendation**: [Deploy / Fix Critical Issues / Major Rework Needed]
```

---

## Iteration Protocol

After initial analysis, use these follow-up patterns:

### Pattern 1: Deep Dive on Specific Component

```markdown
## Deep Dive Request: [Component Name]

**Original System**: [System name from initial analysis]
**Component**: [Specific subsystem/feature to analyze]

**Focus Areas**:
1. [Specific aspect to investigate]
2. [Another aspect]

**Context from System** (maintained):
[Brief excerpt from original analysis showing how this component fits]

**Required Depth**:
- Code-level analysis of [files]
- Pattern examination in [modules]
- Integration analysis with [systems]

Please analyze while maintaining full system context.
```

### Pattern 2: Cross-System Comparison

```markdown
## Cross-System Comparison Request

**Systems**: [System A] vs [System B]
**Comparison Focus**: [What to compare - architecture/patterns/APIs/etc.]

**Specific Questions**:
1. How do their [aspect] approaches differ?
2. Which implementation of [feature] is better and why?
3. Can [System A's approach] be adopted by [System B]?

**Evidence Required**:
- Side-by-side code/doc quotes
- Pattern comparison with file references
- Integration compatibility analysis

Maintain full context of both systems.
```

### Pattern 3: Integration Feasibility

```markdown
## Integration Feasibility Analysis

**System A**: [Name and key capabilities]
**System B**: [Name and key capabilities]
**Integration Goal**: [What you want to achieve]

**Analysis Required**:
1. Identify integration points in both systems (with file refs)
2. Map data flows and transformations needed
3. Assess compatibility (protocols, data formats, APIs)
4. Identify gaps that must be addressed
5. Estimate integration complexity

**Output Needed**:
- Integration architecture diagram (textual)
- Required changes in each system (with file/line refs)
- Risk assessment with mitigation strategies
```

---

```

### Template for Multi-System Comparative Analysis

```markdown
# Multi-System Workflow Analysis: [LIST SYSTEMS]

## AI Persona & Expertise

You are a **System Integration Architect** specializing in:
- Multi-system workflow orchestration
- Pattern analysis across codebases
- Integration opportunity identification
- Cross-platform compatibility assessment
- Architectural synthesis and harmonization

You must analyze multiple systems simultaneously while maintaining complete context for each.

---

## Critical Directive: Multi-System Context Preservation

**[STRICT]** You are analyzing [N] workflow systems. You MUST:

1. **Maintain separate context for each system**
   - Track which documentation/code belongs to which system
   - Reference systems by name in every finding
   - Never confuse patterns between systems

2. **Identify cross-system patterns**
   - Note when multiple systems use similar approaches
   - Highlight unique innovations in each system
   - Map integration opportunities

3. **Provide comparative evidence**
   - Quote from each system being compared
   - Reference specific files from each system
   - Show pattern differences side-by-side

4. **Enable synthesis**
   - Recommend best-of-breed patterns
   - Identify complementary capabilities
   - Suggest integration architectures

---

## SYSTEM CONTENT

### System 1: [NAME]

[FULL SYSTEM CONTENT AS PER SINGLE SYSTEM TEMPLATE]

---

### System 2: [NAME]

[FULL SYSTEM CONTENT AS PER SINGLE SYSTEM TEMPLATE]

---

[REPEAT FOR EACH SYSTEM]

---

## Comparative Analysis Framework

### Phase 1: Individual System Comprehension

For each system, confirm:
- [ ] System purpose and scope understood
- [ ] Architecture reviewed
- [ ] Key components identified
- [ ] Documentation assessed

**Confirmation Grid**:
| System | Purpose | Architecture | Key Components | Doc Quality |
|--------|---------|--------------|----------------|-------------|
| [Name] | [summary] | [pattern] | [list] | [score] |

### Phase 2: Cross-System Pattern Analysis

#### Pattern Dimension 1: Architecture Approaches

**Task**: Compare how each system structures its architecture.

**Output Format**:
```markdown
### Architecture Pattern Comparison

| System | Pattern | Files | Strengths | Weaknesses |
|--------|---------|-------|-----------|------------|
| Sys A | [pattern name] | [key files] | [with quotes] | [with quotes] |
| Sys B | [pattern name] | [key files] | [with quotes] | [with quotes] |

**Best Practice Identified**: [Which system's approach is better for what use case]
- Evidence: System A `file:path` vs System B `file:path`
- Recommendation: [How to harmonize or when to use each]
```

#### Pattern Dimension 2: Integration Mechanisms

Compare how systems handle integrations (APIs, protocols, data exchange).

#### Pattern Dimension 3: Error Handling Strategies

Compare robustness and error handling patterns.

#### Pattern Dimension 4: Documentation Standards

Compare documentation completeness and quality.

### Phase 3: Integration Opportunity Identification

```markdown
## Integration Opportunities

### Opportunity 1: [Description]

**Systems Involved**: [System A] + [System B]
**Integration Point**: 
- System A: File `X`, Feature: [capability]
- System B: File `Y`, Feature: [capability]

**Value Proposition**: [What this integration enables]

**Technical Feasibility**: [High/Medium/Low]
- Evidence: API compatibility [quote both APIs]
- Gap: [what needs to be built]
- Effort: [estimate]

**Recommendation**: [Proceed/Investigate/Skip]
```

### Phase 4: Synthesis & Best-of-Breed

```markdown
## Synthesized Best Practices

### Category: [e.g., "Configuration Management"]

**Best Practice**: [Description]
**Source**: [System that does this well]
**Evidence**: File `path`, "[quote]"
**Adoption Recommendation**:
- For [System B]: [How to implement this pattern]
- For [System C]: [How to implement this pattern]
**Impact**: [Benefits of standardization]
```

---

## Output Format for Multi-System Analysis

### Part 1: Executive Summary

```markdown
# Multi-System Analysis Summary

## Systems Analyzed
1. [System A]: [purpose] - Quality: X/10
2. [System B]: [purpose] - Quality: X/10
3. [System C]: [purpose] - Quality: X/10

## Key Findings
- **Strongest System Overall**: [Name] - Score X/10
- **Best Architecture**: [Name] - Evidence: [file ref]
- **Best Integration Capabilities**: [Name] - Evidence: [file ref]
- **Best Documentation**: [Name] - Evidence: [file ref]

## Integration Opportunities
1. [Opportunity] - Value: High, Feasibility: [score]
2. [Opportunity] - Value: Med, Feasibility: [score]

## Unified Recommendations
- Standardize on [pattern] from [System] for [use case]
- Integrate [System A] + [System B] via [approach]
- Improve [System C's] [aspect] using [System A's pattern]
```

### Part 2: System-by-System Scorecards

[Use single-system scorecard format for each]

### Part 3: Comparative Matrix

```markdown
## Comparative Analysis Matrix

| Dimension | System A | System B | System C | Best-in-Class |
|-----------|----------|----------|----------|---------------|
| Architecture | Score, Pattern | Score, Pattern | Score, Pattern | [System] because [evidence] |
| Implementation | Score, Pattern | Score, Pattern | Score, Pattern | [System] because [evidence] |
| Integration | Score, Pattern | Score, Pattern | Score, Pattern | [System] because [evidence] |
| Documentation | Score, Pattern | Score, Pattern | Score, Pattern | [System] because [evidence] |
```

### Part 4: Integration Architecture

```markdown
## Proposed Integration Architecture

### Integration 1: [System A] ↔ [System B]

**Architecture Pattern**: [MCP / API / Shared DB / Event-driven / etc.]

**Data Flow**:
```
[System A Component] 
    ↓ [Protocol/API]
[Integration Layer]
    ↓ [Protocol/API]
[System B Component]
```

**Implementation Requirements**:
- System A Changes:
  - File: `path`, Add: [feature], Evidence: [current state quote]
- System B Changes:
  - File: `path`, Add: [feature], Evidence: [current state quote]
- New Components:
  - [Adapter/Bridge component], Purpose: [description]

**Benefits**: [What this enables]
**Effort**: [S/M/L/XL]
**Priority**: [Critical/High/Med/Low]
```

### Part 5: Unified Best Practices Guide

```markdown
## Best Practices Synthesis

### Practice 1: [Name]
**Source**: [System that does this]
**Pattern**: [Description]
**Evidence**: File `path`, "[quote]"
**Adoption Guide**:
- For teams using [System A]: [How to apply]
- For teams using [System B]: [How to apply]
**Benefits**: [Why this matters]

[Repeat for top 5-10 practices]
```

---

```

---

## Section 3: Analysis Parameter Configuration

### Select Analysis Depth

**Quick Assessment** (30 min):
- [ ] README and main documentation only
- [ ] Architecture overview
- [ ] Top 5 strengths/weaknesses
- [ ] High-level scorecard

**Standard Analysis** (1-2 hours):
- [ ] All documentation
- [ ] Directory structure analysis
- [ ] Sample code review (5-10 files)
- [ ] All 4 dimensions
- [ ] Detailed recommendations

**Deep Dive** (3-4 hours):
- [ ] Complete documentation
- [ ] Comprehensive code review (20+ files)
- [ ] All dimensions + custom criteria
- [ ] Integration analysis
- [ ] Implementation roadmap

### Select Custom Criteria (Optional)

Add domain-specific analysis dimensions:
- [ ] MCP Protocol Compliance
- [ ] RAG Quality (for knowledge systems)
- [ ] Agent Architecture (for agent systems)
- [ ] Workflow Orchestration Patterns
- [ ] Template System Extensibility
- [ ] Multi-tenant Support
- [ ] Security & Authentication
- [ ] Performance & Scalability
- [ ] Observability & Monitoring

### Define Integration Goals (If Applicable)

If analyzing for integration:
- **Primary Integration Goal**: [What you want to achieve]
- **Systems to Integrate**: [System A] + [System B] + ...
- **Integration Type**: [MCP / API / Shared Data / Event-driven / Embedded]
- **Success Criteria**: [How to measure integration success]

---

## Section 4: Context Gathering Checklist

Before generating your prompt, ensure you have:

### For Each System
- [ ] Complete README.md text
- [ ] Architecture/design documentation
- [ ] Directory structure (tree output or manual listing)
- [ ] Key code samples (5-10 representative files)
- [ ] Configuration examples
- [ ] API/protocol definitions (if applicable)
- [ ] Integration examples (if any)
- [ ] Test patterns (if any)

### System Metadata
- [ ] System name and purpose
- [ ] Repository path
- [ ] Version or last update date
- [ ] Core technologies/frameworks
- [ ] Key dependencies

### Analysis Parameters
- [ ] Analysis depth selected
- [ ] Dimensions to analyze identified
- [ ] Custom criteria defined (if any)
- [ ] Integration goals specified (if applicable)
- [ ] Output format preferences noted

---

## Section 5: Generated Prompt Assembly

**Instructions**: 
1. Choose template (Single System or Multi-System)
2. Fill in all [PLACEHOLDERS] with gathered content
3. Remove optional sections if not needed
4. Ensure all documentation is complete (not summarized)
5. Copy the assembled prompt
6. Submit to AI system

**Quality Checklist Before Submitting**:
- [ ] All system documentation included (not summarized)
- [ ] Directory structures provided
- [ ] Code samples included with file paths
- [ ] Analysis dimensions clearly specified
- [ ] Output format defined
- [ ] Evidence requirements explicit
- [ ] No [PLACEHOLDERS] remaining

---

## Section 6: Iteration Patterns

### After Initial Analysis

**Validation Checklist**:
- [ ] Did AI reference all major components of each system?
- [ ] Are all findings backed by file/line references?
- [ ] Are quotes accurate and properly attributed?
- [ ] Are recommendations specific and actionable?
- [ ] Are scores justified with calculations?

**Common Follow-Up Needs**:

1. **Deeper Component Analysis**: Use "Deep Dive" iteration template
2. **Integration Feasibility**: Use "Integration Feasibility" template
3. **Pattern Comparison**: Use "Cross-System Comparison" template
4. **Implementation Guidance**: Request step-by-step implementation for specific recommendations

---

## Best Practices

### For System Context Gathering

1. **Always include complete documentation** - Never summarize READMEs or architecture docs
2. **Provide directory structure** - Helps AI understand system organization
3. **Include representative code** - 5-10 key files that show patterns
4. **Note what's missing** - Explicitly state if architecture docs don't exist
5. **Version information** - Include version/date for reproducibility

### For Analysis Requests

1. **Be specific about goals** - What decisions will this analysis inform?
2. **Define success criteria** - What makes a good/bad system in your context?
3. **Request evidence** - Always demand file/line references
4. **Enable comparison** - If analyzing multiple systems, request comparative tables
5. **Plan for iteration** - First pass is broad, follow-ups go deep

### For Multi-System Analysis

1. **Maintain clear attribution** - Every finding must specify which system
2. **Use comparison tables** - Easy to scan and compare
3. **Identify unique strengths** - What does each system do best?
4. **Map integration points** - Where can systems connect?
5. **Synthesize best practices** - What patterns should be standardized?

---

## Quick Start Workflow

### For Single System Analysis

1. **Gather context** (10 min):
   - Copy full README.md
   - Run `tree -L 3` and copy output
   - Copy 5 key code files

2. **Select template** (2 min):
   - Use "Base Template for Single System Analysis"

3. **Fill placeholders** (10 min):
   - Paste documentation
   - Paste directory structure
   - Paste code samples
   - Specify analysis focus

4. **Submit to AI** (1 min):
   - Copy complete prompt
   - Paste into AI system
   - Wait for analysis

5. **Review & iterate** (variable):
   - Validate findings
   - Request deep dives as needed

### For Multi-System Comparison

1. **Gather context for all systems** (20-30 min per system)
2. **Select multi-system template** (2 min)
3. **Fill placeholders for each system** (20-30 min total)
4. **Define comparison criteria** (5 min)
5. **Submit to AI** (1 min)
6. **Review comparative analysis** (variable)
7. **Request integration feasibility** (if applicable)

---

## Example Use Cases

### Use Case 1: Evaluating MCP Server Quality

**Goal**: Assess if Archon or mcp-crawl4ai-rag is better for your knowledge management needs

**Approach**: 
- Use multi-system template
- Focus on: Architecture, MCP compliance, RAG quality, Integration capabilities
- Request comparative scorecard
- Request integration feasibility between the two

**Time**: 2-3 hours (context gathering + AI analysis)

---

### Use Case 2: Learning Workflow Patterns

**Goal**: Understand how SuperTemplate implements its 23-protocol workflow

**Approach**:
- Use single system deep-dive template
- Focus on: Architecture, Workflow orchestration, Documentation
- Request detailed protocol analysis
- Request extensibility assessment

**Time**: 3-4 hours

---

### Use Case 3: Integration Planning

**Goal**: Determine how to integrate Archon's knowledge management with SuperTemplate's workflow protocols

**Approach**:
- Use multi-system template for both
- Focus on: Integration points, API compatibility, Data flows
- Request integration architecture
- Request implementation roadmap

**Time**: 4-5 hours

---

### Use Case 4: Template System Evaluation

**Goal**: Decide if Context Engineering Intro patterns can improve your project

**Approach**:
- Use single system standard analysis
- Focus on: Documentation, Usability, Template quality
- Compare against your current setup (add as "System 2")
- Request adoption roadmap

**Time**: 1-2 hours

---

## Troubleshooting

### Issue: AI Response Too Generic

**Fix**: Add evidence requirements to prompt:
```markdown
**[STRICT] Evidence Protocol:**
Every finding MUST include:
1. System name
2. File path (e.g., `python/src/main.py`)
3. Section/line numbers
4. Exact quote or code snippet
5. Analysis of what this means

Example format:
> **Finding**: [Title]
> **System**: Archon
> **Evidence**: File `python/src/server/main.py`, lines 45-52
> **Quote**: "[exact code/text]"
> **Analysis**: [interpretation]
```

### Issue: AI Misses Key Components

**Fix**: Add comprehension checkpoint:
```markdown
**Before analysis, list all major components:**
- Component 1: [name], Files: [paths], Purpose: [description]
- Component 2: ...

Confirm: "I will analyze all listed components."
```

### Issue: Scores Not Justified

**Fix**: Require calculation breakdown:
```markdown
**Scoring Protocol:**
Every score must show calculation:
- Score: 7/10
- Breakdown: Architecture (2/2) + Patterns (3/4) + Documentation (2/4)
- Justification: [why each subscore]
```

### Issue: Missing Integration Analysis

**Fix**: Add explicit integration questions:
```markdown
**Integration Analysis Required:**
1. List all external systems this connects to (with evidence)
2. For each: What protocol? What data? What files implement it?
3. What integration points are missing?
4. What would be needed to integrate with [target system]?
```

---

## Version History

- **v1.0** - Initial workflow system meta prompt creator
- **Purpose**: Ensure complete system context in AI analysis of INTEGRATE workflows
- **Created**: 2025-11-02
- **Target Systems**: Archon, Context Engineering, MCP Crawl4AI RAG, Ottomator Agents, SuperTemplate

---

## Support & Maintenance

**To improve this creator**:
1. Document successful prompt patterns
2. Note edge cases and solutions
3. Add examples from real analyses
4. Refine templates based on AI feedback
5. Update for new systems in INTEGRATE workspace

**To report issues**:
- Generic AI responses → Check evidence requirements in Section 2
- Missing context → Verify all documentation pasted in Section 5
- Poor comparisons → Review multi-system template formatting
- Integration gaps → Use integration feasibility follow-up template
