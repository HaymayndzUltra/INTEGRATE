"""
Shared Structured Logging Package
Based on Archon's structured logging patterns, simplified for general use.

Event naming convention: {module}_{noun}_{verb_past_tense}
Examples:
    - agent_work_order_created
    - git_branch_created
    - workflow_phase_started
    - operation_completed
"""

from collections.abc import MutableMapping
from typing import Any, Optional

import structlog
from structlog.contextvars import bind_contextvars, clear_contextvars


def configure_structured_logging(log_level: str = "INFO") -> None:
    """Configure structlog with console rendering.

    Event naming convention: {module}_{noun}_{verb_past_tense}
    Examples:
        - agent_work_order_created
        - git_branch_created
        - workflow_phase_started
        - operation_completed

    Args:
        log_level: Minimum log level (DEBUG, INFO, WARNING, ERROR)

    Example:
        >>> configure_structured_logging("INFO")
        >>> logger = get_logger(__name__)
        >>> logger.info("operation_completed", duration_ms=123)
    """
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.dev.ConsoleRenderer(),
        ],
        wrapper_class=structlog.stdlib.BoundLogger,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )


def bind_context(context_id: str, **kwargs: Any) -> None:
    """Bind context variables to the current logging context.

    All logs in this context will include the bound variables automatically.
    Convenience wrapper around structlog.contextvars.bind_contextvars.

    Args:
        context_id: Primary context identifier (e.g., request_id, work_order_id)
        **kwargs: Additional context variables to bind

    Examples:
        >>> bind_context("req-123", user_id="user-456")
        >>> logger.info("operation_started")
        >>> # Log will include context_id="req-123" and user_id="user-456" automatically
    """
    bind_contextvars(context_id=context_id, **kwargs)


def clear_context() -> None:
    """Clear the logging context.

    Should be called when context execution completes to prevent
    context leakage to other operations.

    Examples:
        >>> try:
        ...     bind_context("req-123")
        ...     # ... execute operation ...
        ... finally:
        ...     clear_context()
    """
    clear_contextvars()


def get_logger(name: Optional[str] = None) -> structlog.stdlib.BoundLogger:
    """Get a structured logger instance.

    Args:
        name: Optional name for the logger (typically __name__)

    Returns:
        Configured structlog logger

    Examples:
        >>> logger = get_logger(__name__)
        >>> logger.info("operation_completed", duration_ms=123)
        >>> logger.error("operation_failed", error="connection timeout")
    """
    return structlog.get_logger(name)  # type: ignore[no-any-return]

