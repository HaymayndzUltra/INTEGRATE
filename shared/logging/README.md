# Shared Structured Logging Package
# Logging Guidelines and Best Practices

## Philosophy

Logs are optimized for AI agent consumption and human debugging. Include enough context for an LLM or human to understand and fix issues without additional investigation.

## Quick Start

```python
from shared.logging.structured_logger import (
    configure_structured_logging,
    get_logger,
    bind_context,
    clear_context
)

# Configure logging (call once at application startup)
configure_structured_logging("INFO")

# Get a logger
logger = get_logger(__name__)

# Use structured logging
logger.info("operation_completed", duration_ms=123, result="success")
```

## Event Naming Convention

Use `snake_case` format: `{module}_{noun}_{verb_past_tense}`

**Good Examples:**
- `agent_work_order_created`
- `git_branch_created`
- `workflow_phase_started`
- `operation_completed`
- `api_call_succeeded`

**Bad Examples:**
- `connected` (too vague)
- `done` (doesn't describe what)
- `success` (not descriptive)
- `error` (too generic)

## Logging Levels

Use appropriate levels:

- **DEBUG**: Diagnostic information for detailed troubleshooting
- **INFO**: Normal operations, important events
- **WARNING**: Recoverable issues, deprecated usage
- **ERROR**: Non-fatal errors that need attention
- **EXCEPTION**: Use `logger.exception()` in except blocks (includes stack trace)

## Required Rules (MUST)

### 1. Use Structured Logging

Always use keyword arguments, never string formatting:

```python
# ✅ GOOD
logger.info("user_created", user_id="123", role="admin")

# ❌ BAD
logger.info(f"User {user_id} created")
```

### 2. Use logger.exception() in Except Blocks

```python
try:
    result = await operation()
except ValueError as e:
    logger.exception("operation_failed", expected="int", received=type(value).__name__)
    raise
```

### 3. Include Context

Always include relevant IDs and context:
- Request IDs
- User IDs
- Resource IDs
- Operation identifiers

### 4. Mask Sensitive Data

Never log passwords, API keys, or tokens:

```python
# ✅ GOOD
logger.info("api_call", api_key=api_key[:8] + "...")

# ❌ BAD
logger.info("api_call", api_key=api_key)
```

## Recommended Patterns

### Tool Execution

```python
logger.info("tool_execution_started", tool=name, params=params)
try:
    result = await tool.execute(params)
    logger.info("tool_execution_completed", tool=name, duration_ms=duration)
except ToolError as e:
    logger.exception("tool_execution_failed", tool=name, retry_count=count)
    raise
```

### External API Calls

```python
logger.info(
    "api_call",
    provider="openai",
    endpoint="/v1/chat",
    status=200,
    duration_ms=1245.5,
    tokens={"prompt": 245, "completion": 128}
)
```

### State Transitions

```python
logger.info(
    "state_transition",
    resource_id=resource_id,
    old_state="pending",
    new_state="completed"
)
```

### Performance Metrics

```python
import time

start = time.time()
# ... operation ...
duration_ms = (time.time() - start) * 1000
logger.info("operation_completed", duration_ms=duration_ms)
```

## Context Binding

Use context binding for operations that span multiple functions:

```python
from shared.logging.structured_logger import bind_context, clear_context

try:
    bind_context(request_id="req-123", user_id="user-456")
    # All logs in this block will include request_id and user_id
    process_request()
finally:
    clear_context()
```

## DO NOT

- ❌ **DO NOT** use string formatting in logs
- ❌ **DO NOT** log sensitive data (passwords, keys, tokens)
- ❌ **DO NOT** spam logs in loops (log batch summaries instead)
- ❌ **DO NOT** silently catch exceptions (always log with `logger.exception()`)
- ❌ **DO NOT** use vague event names (be specific)

## Installation

Add to your workflow's dependencies:

```toml
# pyproject.toml
[project]
dependencies = [
    "structlog>=24.4.0",
]
```

## Integration Example

```python
from shared.logging.structured_logger import (
    configure_structured_logging,
    get_logger,
    bind_context,
    clear_context
)

# At application startup
configure_structured_logging("INFO")

# In your code
logger = get_logger(__name__)

async def process_request(request_id: str, user_id: str):
    try:
        bind_context(request_id=request_id, user_id=user_id)
        
        logger.info("request_processing_started")
        
        # ... your logic ...
        
        logger.info("request_processing_completed", duration_ms=123)
    except Exception as e:
        logger.exception("request_processing_failed", error=str(e))
        raise
    finally:
        clear_context()
```

