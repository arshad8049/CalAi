import os

# Database connection string (e.g., Supabase Postgres URL or local Postgres)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/calai_db")

# Path to the DeepSeek AI model
DEEPSEEK_MODEL_PATH = os.getenv("DEEPSEEK_MODEL_PATH", "/path/to/deepseek/model")

# API prefix for all endpoints
API_PREFIX = "/api"