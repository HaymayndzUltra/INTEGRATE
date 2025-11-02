# Dependency Version Matrix
# Shared dependency versions across all INTEGRATE workflows

# This document defines standardized versions for common dependencies used across
# multiple workflows to prevent version conflicts and ensure compatibility.

# =============================================================================
# Core Python Libraries
# =============================================================================

# Web Framework
fastapi==0.115.11           # Latest stable version with security patches
uvicorn==0.32.1             # ASGI server (compatible with FastAPI 0.115+)

# Data Validation & Settings
pydantic==2.10.6            # Latest stable 2.x version
pydantic-settings==2.7.1     # Settings management for Pydantic
pydantic-ai==0.0.22         # Pydantic AI framework

# HTTP Client
httpx==0.28.1               # HTTP client library
requests==2.32.3             # Legacy HTTP client (if needed)

# =============================================================================
# LLM Providers
# =============================================================================

# OpenAI
openai==1.71.0               # Latest OpenAI SDK version

# Anthropic (if used)
anthropic==0.40.0            # Anthropic Claude SDK

# Google Gemini (if used)
google-generativeai==0.8.3   # Google Gemini SDK

# =============================================================================
# Database & Vector Stores
# =============================================================================

# Supabase
supabase==2.15.1             # Supabase Python client

# PostgreSQL drivers
psycopg2-binary==2.9.10      # PostgreSQL adapter
asyncpg==0.30.0              # Async PostgreSQL driver

# Vector databases
pgvector==0.3.4              # PostgreSQL vector extension (if using)

# Neo4j (for knowledge graphs)
neo4j==5.26.0                # Neo4j Python driver

# =============================================================================
# Web Crawling & Processing
# =============================================================================

# Crawl4AI
crawl4ai==0.7.4              # Web crawling library

# Document Processing
docling==1.0.0               # Document processing (if used)

# =============================================================================
# MCP (Model Context Protocol)
# =============================================================================

mcp==1.12.2                  # MCP SDK

# =============================================================================
# Embeddings & ML
# =============================================================================

# Sentence Transformers
sentence-transformers>=4.1.0  # Minimum version for embeddings

# OpenAI Embeddings
openai-embeddings==0.1.0     # OpenAI embeddings wrapper (if used)

# =============================================================================
# Utilities
# =============================================================================

# Environment Variables
python-dotenv==1.0.1        # .env file loading

# Logging
structlog==24.4.0            # Structured logging

# Async
asyncio==3.4.3               # Async utilities (if needed)

# =============================================================================
# Development & Testing
# =============================================================================

# Testing
pytest==8.3.4                # Testing framework
pytest-asyncio==0.24.0       # Async test support
pytest-cov==6.0.0            # Coverage reporting

# Linting & Formatting
black==24.10.0                # Code formatting
ruff==0.7.3                  # Fast Python linter
mypy==1.13.0                  # Type checking

# =============================================================================
# Node.js Dependencies (for Frontend)
# =============================================================================

# Note: These are managed via package.json, but common versions are listed here
# for reference across workflows

# React & UI
react==18.3.1
typescript==5.7.2

# Testing
vitest==2.1.8
@testing-library/react==16.1.0

# =============================================================================
# Version Policy
# =============================================================================

# 1. Major versions (x.y.z): Only update when breaking changes are acceptable
# 2. Minor versions (x.y.z): Update regularly for new features and security patches
# 3. Patch versions (x.y.z): Update immediately for security fixes

# =============================================================================
# Compatibility Notes
# =============================================================================

# FastAPI 0.115+ requires Python 3.12+
# Pydantic 2.x requires Python 3.10+
# OpenAI SDK 1.71+ requires Python 3.9+
# Supabase 2.15+ requires Python 3.9+

# =============================================================================
# Migration Guide
# =============================================================================

# To migrate workflows to use these versions:
# 1. Update requirements.txt or pyproject.toml dependencies
# 2. Test thoroughly to ensure compatibility
# 3. Update any deprecated API calls
# 4. Run full test suite

