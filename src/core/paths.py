"""Centralized filesystem path configurations using pathlib."""

from pathlib import Path

# Anchored to the repository, not to the current directory, so scripts work from any folder.
WORKSPACE_ROOT = Path(__file__).resolve().parents[2]

CONFIG_DIR = WORKSPACE_ROOT / "config"
SETTINGS_YAML = CONFIG_DIR / "settings.yaml"
DATASOURCE_YAML = CONFIG_DIR / "datasource.yaml"
LOGGING_YAML = CONFIG_DIR / "logging.yaml"

DATABASE_DIR = WORKSPACE_ROOT / "database"
SCHEMA_SQL = DATABASE_DIR / "schema.sql"
DB_FILE = DATABASE_DIR / "research_os.db"

DOCS_DIR = WORKSPACE_ROOT / "docs"
LOGS_DIR = WORKSPACE_ROOT / "logs"
OUTPUT_DIR = WORKSPACE_ROOT / "output"
WORKSPACE_DIR = WORKSPACE_ROOT / "workspace"
SCRIPTS_DIR = WORKSPACE_ROOT / "scripts"
SRC_DIR = WORKSPACE_ROOT / "src"
PAPERS_DIR = WORKSPACE_ROOT / "papers"
DATA_DIR = WORKSPACE_ROOT / "data"
HANDOFF_DIR = WORKSPACE_ROOT / "handoff"
RULES_DIR = WORKSPACE_ROOT / "rules"
CONFIG_EXPECTED = CONFIG_DIR / "expected_numbers.yaml"
CLAIMS_REGISTER = CONFIG_DIR / "claims_register.yaml"
MANUSCRIPT_DIR = PAPERS_DIR / "manuscript"
TABLES_DIR = OUTPUT_DIR / "tables"
