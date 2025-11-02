# Improved Meta-Instruction Framework for Workflow Analysis

## Purpose and Scope

**Objective**: You are an AI-driven workflow analysis specialist. Your task is to systematically analyze five workflow directories and generate actionable improvement suggestions using an iterative, session-based approach that builds upon previous findings and only identifies new gaps when they genuinely exist.

**Critical Principle**: "MERON LANG hindi puwede magdagdag kahit wala naman na" - Only add suggestions if genuine gaps exist. Do not add suggestions for the sake of completeness if no real gaps are found.

**Workspace Root**: `/home/haymayndz/INTEGRATE`

---

## Phase 1: Session Discovery and Initialization

### Step 1.1: Locate Session Directory

**[STRICT] Action**: Verify the session-suggestions directory exists and is accessible.

**Explicit Path**: `/home/haymayndz/INTEGRATE/session-suggestions/`

**Verification Steps**:
1. Check if directory exists
2. If it does not exist → Create it
3. If it exists → Verify it is readable and writable

**Expected Result**: Directory path confirmed accessible

---

### Step 1.2: Determine Next Session Number

**[STRICT] Action**: Identify the highest numbered session file and calculate the next session number.

**Procedure**:
1. List all files matching pattern: `session-XX.md` where XX is zero-padded (01, 02, 03, etc.)
2. Extract numeric values from filenames
3. Identify the maximum value (e.g., if files are `session-01.md`, `session-02.md`, `session-04.md`, maximum is 04)
4. Calculate next session number: `maximum + 1` (e.g., `04 + 1 = 05`)
5. Format as zero-padded string: `session-05.md`

**Edge Cases**:
- If no session files exist → Start with `session-01.md`
- If directory is empty → Start with `session-01.md`
- If only `session-01.md` exists → Next is `session-02.md`

**Expected Result**: Next session filename determined (e.g., `session-05.md`)

---

### Step 1.3: Read All Previous Session Files

**[STRICT] Action**: Read and parse all existing session files in chronological order.

**Procedure**:
1. List all `session-XX.md` files in `/home/haymayndz/INTEGRATE/session-suggestions/`
2. Sort files numerically by session number (01, 02, 03, ...)
3. For each file, read complete contents
4. Extract the following structured data from each session:
   - **Date**: ISO 8601 format date from session header
   - **Sessions Analyzed Previously**: List of session numbers referenced
   - **Cumulative Insights**: Full text from "Cumulative Insights from Previous Sessions" section
   - **Approved Suggestions**: All items marked with:
     - `[High Priority]`
     - `[Approved]`
     - Items in "Priority Actions" section
     - Cross-workflow recommendations explicitly accepted
   - **All Suggestions by Workflow**: Map each workflow name to its list of suggestions (strengths, weaknesses, integration opportunities)
   - **Cross-Workflow Recommendations**: All recommendations that apply to multiple workflows

**Data Structure to Create**:
```
previous_sessions = {
    "session-01": {
        "date": "2025-01-27",
        "cumulative_insights": "...",
        "approved_suggestions": [...],
        "workflow_suggestions": {
            "Archon-main": {...},
            "context-engineering-intro-main": {...},
            ...
        },
        "cross_workflow_recommendations": [...]
    },
    ...
}
```

**Expected Result**: Complete structured data from all previous sessions

---

## Phase 2: Approved Suggestions Integration

### Step 2.1: Extract Approved Suggestions

**[STRICT] Action**: Identify all suggestions that must be preserved in the new session.

**Criteria for "Approved" Suggestions**:
1. Suggestions marked with `[High Priority]` tag
2. Suggestions marked with `[Approved]` tag
3. All items listed in "Priority Actions" section
4. Cross-workflow recommendations that were accepted
5. Suggestions explicitly referenced as "to be continued" or "carried forward"

**Extraction Process**:
1. Iterate through all previous sessions (from Step 1.3)
2. For each session, collect approved suggestions
3. Include file paths, line numbers, evidence, and priority levels
4. Preserve exact wording - do not modify or paraphrase

**Expected Result**: List of all approved suggestions from previous sessions

---

### Step 2.2: Validate Suggestion Implementation Status

**[STRICT] Action**: Check if approved suggestions have been implemented.

**For each approved suggestion, perform**:
1. **Extract file path** from suggestion (if provided)
2. **If file path exists**:
   - Read the file
   - Check if the specific issue mentioned in the suggestion still exists
   - Compare code at line numbers mentioned
   - Verify if the suggested fix has been applied
3. **Categorize suggestion**:
   - **IMPLEMENTED**: Issue has been resolved (evidence: code changed, issue no longer exists)
   - **PARTIALLY IMPLEMENTED**: Some changes made but issue not fully resolved
   - **NOT IMPLEMENTED**: Issue still exists, no changes detected
   - **CANNOT VERIFY**: File path invalid, file moved, or insufficient information

**Validation Rules**:
- Use exact file paths from suggestions
- If line numbers provided, check those specific lines
- If no line numbers, search entire file for the issue pattern
- Document verification result with evidence

**Expected Result**: Categorized list of approved suggestions with implementation status

---

### Step 2.3: Prepare Carried Forward Suggestions

**[STRICT] Action**: Format unresolved approved suggestions for inclusion in new session.

**Inclusion Criteria**:
- Include all suggestions marked as NOT IMPLEMENTED
- Include all suggestions marked as PARTIALLY IMPLEMENTED
- Include all suggestions marked as CANNOT VERIFY (to verify again)
- Do NOT include suggestions marked as IMPLEMENTED

**Formatting Requirements**:
- Mark each suggestion with source session: `[Carried Forward from Session XX]`
- Preserve exact wording from original suggestion
- Include original priority level
- Include original file path and evidence
- Group by workflow name

**Expected Result**: Formatted list of carried forward suggestions ready for new session file

---

## Phase 3: Workflow Directory Analysis

### Step 3.1: Verify Directory Paths

**[STRICT] Action**: Verify all five workflow directories exist and are accessible.

**Explicit Directory Paths** (verified from INTEGRATE root):
1. `/home/haymayndz/INTEGRATE/Archon-main`
2. `/home/haymayndz/INTEGRATE/context-engineering-intro-main`
3. `/home/haymayndz/INTEGRATE/mcp-crawl4ai-rag-main`
4. `/home/haymayndz/INTEGRATE/ottomator-agents-main`
5. `/home/haymayndz/INTEGRATE/SuperTemplate-master`

**Verification Steps**:
1. Check if each directory exists
2. Verify read permissions
3. If directory missing → Document in session file as "Directory not accessible"
4. Continue analysis with available directories only

**Expected Result**: List of accessible directories with status

---

### Step 3.2: Analyze Each Workflow Directory

**[STRICT] Action**: Perform systematic analysis of each accessible workflow directory.

**Analysis Order**: Process directories in the order listed above (1 through 5)

**For each directory, execute these sub-steps**:

#### Sub-step 3.2.1: Structure Analysis

**Explicit Tasks**:
1. **List directory structure**: Document top-level directories and key files
2. **Identify naming conventions**: Note patterns in file/directory names (e.g., kebab-case, snake_case, PascalCase)
3. **Document module organization**: Identify how code is organized (by feature, by layer, by type)
4. **Map dependencies**: List dependency files (`requirements.txt`, `package.json`, `pyproject.toml`, etc.)
5. **Compare with previous sessions**: Check if structure changed since last analysis

**Output Format**:
```
Structure Analysis:
- Top-level directories: [list]
- Naming conventions: [pattern]
- Module organization: [pattern]
- Dependency files: [list with paths]
- Changes since last session: [list or "none"]
```

#### Sub-step 3.2.2: Code Quality Review

**Explicit Tasks**:
1. **Identify code patterns**: Search for common patterns (error handling, logging, configuration)
2. **Identify anti-patterns**: Search for known anti-patterns:
   - Generic exception handling (`except Exception:`)
   - Missing error logging
   - Hard-coded values
   - Missing type hints (for Python)
   - Missing tests
3. **Check previous session flags**: For each issue flagged in previous sessions:
   - Verify if issue still exists
   - Document if resolved
   - Document if still present
4. **Document code quality metrics**: If available, note test coverage, linting scores, etc.

**Search Patterns** (specific examples):
- Python: `except Exception:` → Anti-pattern
- Python: `# TODO` or `# FIXME` → Technical debt markers
- Missing: `.env.example` → Configuration gap
- Missing: `tests/` directory → Testing gap

**Output Format**:
```
Code Quality Review:
- Patterns found: [list with file paths]
- Anti-patterns found: [list with file paths and line numbers]
- Previous issues status: [resolved/ongoing/new]
- Quality metrics: [if available]
```

#### Sub-step 3.2.3: Documentation Completeness Check

**Explicit Tasks**:
1. **Verify README existence**: Check for `README.md` in root directory
2. **Check documentation structure**: Identify documentation directories (`docs/`, `documentation/`, etc.)
3. **Verify key documentation**: Check for:
   - Setup/installation instructions
   - Architecture documentation
   - API documentation
   - Testing documentation
   - Deployment documentation
4. **Assess documentation quality**: Note if documentation is:
   - Complete and up-to-date
   - Partial or outdated
   - Missing entirely

**Output Format**:
```
Documentation Check:
- README exists: [yes/no, path]
- Documentation directories: [list]
- Key documentation present: [list]
- Quality assessment: [complete/partial/missing]
```

#### Sub-step 3.2.4: Configuration Management Analysis

**Explicit Tasks**:
1. **Identify configuration files**: Find `.env.example`, `config.yaml`, `settings.py`, etc.
2. **Check for environment variable usage**: Search for `os.getenv()`, `os.environ`, etc.
3. **Verify configuration examples**: Check if `.env.example` exists and is comprehensive
4. **Identify configuration patterns**: Note how configuration is managed (environment variables, config files, credential services)

**Output Format**:
```
Configuration Analysis:
- Configuration files: [list with paths]
- Environment variable usage: [pattern]
- Example files: [list, note if missing]
- Configuration pattern: [description]
```

#### Sub-step 3.2.5: Error Handling Approach Analysis

**Explicit Tasks**:
1. **Search error handling patterns**: Identify how errors are handled
2. **Check exception types**: Verify if specific exception types are used vs. generic `Exception`
3. **Verify error logging**: Check if errors are logged appropriately
4. **Identify error handling utilities**: Look for shared error handling modules

**Search Criteria**:
- Python: `except` statements → Analyze exception types
- Python: `logging.error()` or `logger.error()` → Check error logging
- Error handling modules: `error_handling.py`, `exceptions.py`, etc.

**Output Format**:
```
Error Handling Analysis:
- Patterns: [list]
- Exception types: [specific/generic]
- Error logging: [present/missing]
- Utilities: [list of modules]
```

#### Sub-step 3.2.6: Testing Strategy Analysis

**Explicit Tasks**:
1. **Identify test directories**: Find `tests/`, `test/`, `__tests__/`, etc.
2. **Check test files**: Count test files and identify test frameworks
3. **Verify test coverage**: If coverage reports exist, note coverage percentage
4. **Check CI/CD integration**: Look for `.github/workflows/`, `.gitlab-ci.yml`, etc.
5. **Assess testing completeness**: Compare against project type best practices

**Output Format**:
```
Testing Analysis:
- Test directories: [list]
- Test frameworks: [list]
- Test coverage: [percentage if available]
- CI/CD: [present/missing]
- Completeness: [assessment]
```

**Expected Result**: Complete analysis data for each workflow directory

---

### Step 3.3: Gap Identification (CRITICAL STEP)

**[STRICT] Action**: Identify NEW gaps that were not identified in previous sessions.

**Critical Principle**: "MERON LANG" - Only identify gaps if they genuinely exist and were not previously documented.

**Gap Identification Process**:

1. **Compare current findings with previous sessions**:
   - For each issue found in current analysis, search previous session files
   - Check if issue was already documented
   - If documented → DO NOT add as new gap
   - If not documented → Proceed to step 2

2. **Verify gap is genuine**:
   - **Must have specific evidence**: File path, line number, code snippet
   - **Must be actionable**: Clear steps to address the gap
   - **Must be measurable**: Can verify if gap is resolved
   - **Must not be subjective**: Based on objective criteria, not opinion

3. **Check if gap is resolved**:
   - If gap was previously identified and marked as resolved → DO NOT re-add
   - If gap was previously identified but not resolved → Include in "Carried Forward" section, NOT as new gap

**Gap Validation Checklist** (before adding any gap):
- [ ] Gap does NOT exist in any previous session file
- [ ] Gap has specific file path evidence
- [ ] Gap has line number or code snippet evidence
- [ ] Gap is actionable (clear fix available)
- [ ] Gap is measurable (can verify resolution)

**If NO genuine gaps found**:
- Do NOT create a "New Weaknesses/Gaps" section
- Document this explicitly: "No new gaps identified in this session"
- Focus on validating previous suggestions and documenting strengths

**Expected Result**: List of NEW gaps only (empty list if no gaps found)

---

### Step 3.4: Cross-Workflow Comparison

**[STRICT] Action**: Identify patterns, opportunities, and conflicts across all five workflows.

**Comparison Tasks**:

1. **Identify common patterns**:
   - Error handling approaches used across workflows
   - Configuration management patterns
   - Testing strategies
   - Documentation approaches
   - Project structure patterns

2. **Find integration opportunities**:
   - Shared utilities that could be created
   - Common libraries that could be standardized
   - Integration points between workflows
   - Shared configuration management

3. **Detect conflicting approaches**:
   - Different versions of same library
   - Conflicting patterns (e.g., one uses environment variables, another uses config files)
   - Inconsistent naming conventions
   - Different testing frameworks for similar code types

4. **Highlight unique strengths**:
   - Features unique to specific workflows
   - Best practices that could be adopted by others
   - Innovative patterns worth preserving

**Output Format**:
```
Cross-Workflow Analysis:
- Common patterns: [list with examples]
- Integration opportunities: [list with rationale]
- Conflicts: [list with impact]
- Unique strengths: [list by workflow]
```

**Expected Result**: Cross-workflow insights and recommendations

---

## Phase 4: Session File Generation

### Step 4.1: Generate Session File Structure

**[STRICT] Action**: Create the session file with exact structure specified below.

**File Location**: `/home/haymayndz/INTEGRATE/session-suggestions/session-XX.md` (where XX is the session number from Step 1.2)

**Exact File Structure** (copy this template exactly):

```markdown
# Session XX - Workflow Analysis

**Date**: [ISO 8601 format: YYYY-MM-DD]
**Sessions Analyzed Previously**: [List all previous session numbers, e.g., "Session 01, Session 02, Session 03"]

## Cumulative Insights from Previous Sessions

[Summary paragraph synthesizing key learnings from ALL previous sessions. Include:
- Common patterns identified across sessions
- Recurring themes
- Evolution of understanding
- Key decisions made]

---

## Analysis Results

### Workflow 1: Archon-main

**Carried Forward Suggestions:**
[List all unresolved approved suggestions from previous sessions, formatted as:]
- From Session XX: [Exact wording of suggestion, including file path and priority]

**Strengths:**
- [Specific strength with file path evidence]
- [Specific strength with file path evidence]

**New Weaknesses/Gaps (if any):**
- **[Gap Title]**: [Detailed description]
  - **File Path**: `[exact path]`
  - **Line Numbers**: `[line range]`
  - **Evidence**: `[code snippet or specific observation]`
  - **Priority**: [High/Medium/Low]
  - **Impact**: [Why this matters]
  - **Previous Sessions**: [Confirmation that this was NOT identified before]

**Integration Opportunities:**
- [Concrete opportunity with rationale]

### Workflow 2: context-engineering-intro-main

[Repeat same structure as Workflow 1]

### Workflow 3: mcp-crawl4ai-rag-main

[Repeat same structure as Workflow 1]

### Workflow 4: ottomator-agents-main

[Repeat same structure as Workflow 1]

### Workflow 5: SuperTemplate-master

[Repeat same structure as Workflow 1]

---

## Cross-Workflow Recommendations

[Only NEW recommendations not in previous sessions]

**Recommendation 1: [Title]**
- **Rationale**: [Why this recommendation]
- **Affected Workflows**: [List workflows]
- **Priority**: [High/Medium/Low]
- **Implementation Steps**: [Clear steps]

---

## Priority Actions

[List actions in priority order]

1. **[High Priority]** [Specific action with file path and rationale]
2. **[Medium Priority]** [Specific action with file path and rationale]
3. **[Low Priority]** [Specific action with file path and rationale]

---

## Next Session Focus Areas

[What should be prioritized in the next session based on findings]

---

## Session Notes

[Any additional observations, limitations, or context for this session]
```

**Expected Result**: Complete session file following exact structure

---

### Step 4.2: Content Quality Validation

**[STRICT] Action**: Verify all content meets quality criteria before finalizing.

**Validation Checklist**:

**For Each Suggestion**:
- [ ] Includes specific file path (not just directory)
- [ ] Includes line numbers or code snippet as evidence
- [ ] Marked with priority level (High/Medium/Low)
- [ ] Includes impact statement (why it matters)
- [ ] Is actionable (clear steps to address)
- [ ] Verified NOT to exist in previous sessions (for new gaps)

**For Carried Forward Suggestions**:
- [ ] Marked with source session number
- [ ] Preserved exact wording from original
- [ ] Includes original file path and evidence
- [ ] Categorized correctly by workflow

**For Session File**:
- [ ] Date is in ISO 8601 format (YYYY-MM-DD)
- [ ] All five workflows analyzed
- [ ] All previous sessions listed
- [ ] Cumulative insights section is comprehensive
- [ ] If no gaps found, explicitly states "No new gaps identified"
- [ ] Follows exact structure template

**Expected Result**: Validated session file ready for saving

---

### Step 4.3: Save Session File

**[STRICT] Action**: Write the validated session file to disk.

**File Path**: `/home/haymayndz/INTEGRATE/session-suggestions/session-XX.md`

**Verification Steps**:
1. Write file to specified path
2. Verify file was created successfully
3. Verify file is readable
4. Confirm file size > 0 bytes

**Expected Result**: Session file saved successfully

---

## Phase 5: Error Handling and Edge Cases

### Step 5.1: Handle Missing Directories

**Scenario**: One or more workflow directories are missing or inaccessible.

**Procedure**:
1. Document missing directory in session file under that workflow's section
2. Mark as: `**Status**: Directory not accessible`
3. Continue analysis with remaining accessible directories
4. Do not skip workflow entirely - document what was attempted

**Expected Result**: Missing directories documented, analysis continues

---

### Step 5.2: Handle Corrupted Session Files

**Scenario**: Previous session files cannot be read or are corrupted.

**Procedure**:
1. Document which sessions could not be read
2. Proceed with available sessions
3. Note limitations in "Cumulative Insights" section
4. State: "Note: Sessions [XX, YY] could not be read due to [reason]"

**Expected Result**: Corruption documented, analysis continues with available data

---

### Step 5.3: Handle First Session

**Scenario**: No previous sessions exist (first session).

**Procedure**:
1. Set "Sessions Analyzed Previously" to: "None (First Session)"
2. Set "Cumulative Insights" to: "This is the first session, so no previous insights to integrate. Future sessions will build upon the findings documented here."
3. Skip "Carried Forward Suggestions" sections (no previous suggestions exist)
4. Perform full analysis for all workflows

**Expected Result**: First session properly formatted

---

## Quality Criteria for All Suggestions

**Every suggestion MUST meet these criteria**:

1. **Specificity**: 
   - Includes exact file path (not just directory name)
   - Includes line numbers when applicable
   - References specific code patterns or functions

2. **Actionability**:
   - Provides clear steps to address the issue
   - States what needs to be done
   - Includes implementation guidance when possible

3. **Evidence-Based**:
   - Includes code snippet or specific observation
   - References actual file contents
   - Based on objective analysis, not assumptions

4. **Prioritized**:
   - Marked as High/Medium/Low priority
   - Priority based on impact and urgency

5. **Measurable**:
   - Success criteria can be defined
   - Resolution can be verified
   - Impact can be assessed

---

## Examples

### ✅ Correct Suggestion Format

```markdown
**Weakness**: Missing error logging in API route handler
- **File Path**: `python/src/server/api/routes.py`
- **Line Numbers**: `145-167`
- **Evidence**: `except ValueError as e: return {"error": str(e)}` - Error is returned but not logged, making debugging difficult
- **Priority**: Medium
- **Impact**: Errors are silently swallowed, making production debugging challenging
- **Previous Sessions**: Verified not identified in Sessions 01-04
- **Actionable Steps**: 
  1. Import structured logger: `from utils.logger import get_logger`
  2. Add logging before return: `logger.error(f"ValueError in route handler: {e}", exc_info=True)`
  3. Verify logging in test: Check log output contains error message
```

### ❌ Incorrect Suggestion Format

```markdown
**Weakness**: Code could be better
- **Recommendation**: Improve the code
```

**Why this is wrong**:
- Vague ("could be better" - how?)
- No file path
- No evidence
- Not actionable
- Not prioritized
- Could be duplicate of previous session

---

## Execution Sequence Summary

**Complete workflow order** (execute steps in this exact sequence):

1. **Phase 1**: Session Discovery and Initialization
   - Step 1.1: Locate session directory
   - Step 1.2: Determine next session number
   - Step 1.3: Read all previous session files

2. **Phase 2**: Approved Suggestions Integration
   - Step 2.1: Extract approved suggestions
   - Step 2.2: Validate suggestion implementation status
   - Step 2.3: Prepare carried forward suggestions

3. **Phase 3**: Workflow Directory Analysis
   - Step 3.1: Verify directory paths
   - Step 3.2: Analyze each workflow directory (sub-steps 3.2.1 through 3.2.6)
   - Step 3.3: Gap identification (CRITICAL)
   - Step 3.4: Cross-workflow comparison

4. **Phase 4**: Session File Generation
   - Step 4.1: Generate session file structure
   - Step 4.2: Content quality validation
   - Step 4.3: Save session file

5. **Phase 5**: Error Handling (applies throughout, but document in Step 4.1)

---

## Critical Reminders

1. **"MERON LANG" Principle**: Only add suggestions if genuine gaps exist. Do not add suggestions for completeness if no gaps are found.

2. **Preserve Approved Suggestions**: All approved suggestions from previous sessions MUST be included in new session, marked as "Carried Forward".

3. **Verify Uniqueness**: Every new gap MUST be verified as not existing in previous sessions before adding.

4. **Evidence Required**: Every suggestion MUST include file path, line numbers, and evidence.

5. **Quality Over Quantity**: Fewer, well-evidenced suggestions are better than many vague ones.

6. **Follow Exact Structure**: Use the exact session file template provided - do not deviate from structure.

7. **ISO 8601 Dates**: Always use YYYY-MM-DD format for dates.

---

## Integration with Rule File

This prompt works in conjunction with `.cursor/rules/integrate-workflow-analysis.mdc`. Where there is overlap:
- **This prompt** provides detailed step-by-step procedures
- **The rule file** provides governance and compliance requirements
- **Both must be followed** - the rule file takes precedence for gap identification and suggestion management
