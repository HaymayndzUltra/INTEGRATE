# Shared Configuration Package
# README for using shared configuration utilities

This package provides standardized configuration management using `pydantic-settings`.

## Usage

### Basic Usage

```python
from shared.config.base_config import BaseConfig, load_config

# Create a custom config class
class MyWorkflowConfig(BaseConfig):
    # Add workflow-specific fields
    my_api_key: str
    
    # Custom validator
    @field_validator("my_api_key")
    @classmethod
    def validate_api_key(cls, v: str) -> str:
        if not v.startswith("sk-"):
            raise ValueError("API key must start with 'sk-'")
        return v

# Load configuration
config = load_config(MyWorkflowConfig)
print(config.log_level)  # Uses default from BaseConfig
print(config.my_api_key)  # From environment or .env file
```

### Using LLM Configuration

```python
from shared.config.base_config import LLMConfig, load_config

config = load_config(LLMConfig)
# Access: config.llm_provider, config.llm_api_key, config.llm_model
```

### Using Database Configuration

```python
from shared.config.base_config import DatabaseConfig, load_config

config = load_config(DatabaseConfig)
# Access: config.supabase_url, config.database_url, etc.
```

### Combining Configurations

```python
from shared.config.base_config import BaseConfig, LLMConfig, DatabaseConfig

class CompleteConfig(BaseConfig, LLMConfig, DatabaseConfig):
    """Combined configuration."""
    pass

config = load_config(CompleteConfig)
```

## Environment Variables

Create a `.env` file in your workflow root:

```bash
# Common settings
LOG_LEVEL=INFO
SERVICE_DISCOVERY_MODE=local

# LLM settings
LLM_PROVIDER=openai
LLM_API_KEY=your-key-here
LLM_MODEL=gpt-4o-mini

# Database settings
SUPABASE_URL=your-supabase-url
SUPABASE_SERVICE_KEY=your-service-key
```

## Benefits

1. **Type Safety**: Pydantic validates types at runtime
2. **IDE Support**: Autocomplete for configuration fields
3. **Validation**: Automatic validation of values
4. **Documentation**: Self-documenting through type hints
5. **Consistency**: Standardized configuration across workflows

