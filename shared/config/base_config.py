# Shared Configuration Package
# Base settings class using pydantic-settings for type-safe configuration

"""
Base configuration class for all INTEGRATE workflows.

This module provides a standardized way to handle environment variables
and configuration with type safety and validation.
"""

from pydantic_settings import BaseSettings
from pydantic import Field, ConfigDict, field_validator
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv


class BaseConfig(BaseSettings):
    """
    Base configuration class with common settings.
    
    Subclass this for workflow-specific configurations.
    """
    
    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
        env_prefix="",  # No prefix by default
    )
    
    # Common logging configuration
    log_level: str = Field(default="INFO", description="Logging level")
    logfire_enabled: bool = Field(default=False, description="Enable Logfire logging")
    logfire_token: Optional[str] = Field(default=None, description="Logfire token")
    
    # Common service configuration
    service_discovery_mode: str = Field(
        default="local",
        description="Service discovery mode: 'local' or 'docker_compose'"
    )
    
    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, v: str) -> str:
        """Validate log level."""
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if v.upper() not in valid_levels:
            raise ValueError(f"log_level must be one of {valid_levels}")
        return v.upper()
    
    @field_validator("service_discovery_mode")
    @classmethod
    def validate_service_discovery_mode(cls, v: str) -> str:
        """Validate service discovery mode."""
        valid_modes = ["local", "docker_compose"]
        if v.lower() not in valid_modes:
            raise ValueError(f"service_discovery_mode must be one of {valid_modes}")
        return v.lower()


class LLMConfig(BaseSettings):
    """Configuration for LLM providers."""
    
    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )
    
    # LLM Provider
    llm_provider: str = Field(default="openai", description="LLM provider")
    llm_api_key: str = Field(..., description="API key for LLM provider")
    llm_model: str = Field(default="gpt-4o-mini", description="Model name")
    llm_base_url: Optional[str] = Field(
        default=None,
        description="Base URL for LLM API (optional, for custom endpoints)"
    )
    
    # Embedding configuration
    embedding_model: Optional[str] = Field(
        default=None,
        description="Embedding model (if different from LLM model)"
    )


class DatabaseConfig(BaseSettings):
    """Configuration for database connections."""
    
    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )
    
    # Supabase configuration
    supabase_url: Optional[str] = Field(
        default=None,
        description="Supabase project URL"
    )
    supabase_service_key: Optional[str] = Field(
        default=None,
        description="Supabase service role key"
    )
    
    # PostgreSQL configuration
    database_url: Optional[str] = Field(
        default=None,
        description="PostgreSQL connection string"
    )
    
    # Neo4j configuration
    neo4j_uri: Optional[str] = Field(
        default=None,
        description="Neo4j connection URI"
    )
    neo4j_user: Optional[str] = Field(
        default=None,
        description="Neo4j username"
    )
    neo4j_password: Optional[str] = Field(
        default=None,
        description="Neo4j password"
    )


def load_config(config_class: type[BaseSettings], env_file: Optional[Path] = None) -> BaseSettings:
    """
    Load configuration from environment variables and .env file.
    
    Args:
        config_class: Configuration class to instantiate
        env_file: Optional path to .env file (defaults to .env in current directory)
    
    Returns:
        Instance of config_class with loaded values
    
    Raises:
        ValueError: If required configuration is missing
    """
    if env_file:
        load_dotenv(env_file)
    else:
        load_dotenv()
    
    try:
        return config_class()
    except Exception as e:
        error_msg = f"Failed to load configuration: {e}"
        raise ValueError(error_msg) from e

