#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Research-OS Foundation Bootstrapper
Question-driven Research Intelligence Operating System

Run this script to initialize or repair the workspace structure,
default YAML configurations, and SQLite database schemas:
    python bootstrap.py
"""

import sys
from pathlib import Path
import sqlite3

REQUIRED_MAJOR = 3
REQUIRED_MINOR = 11

if sys.version_info < (REQUIRED_MAJOR, REQUIRED_MINOR):
    print(f"CRITICAL ERROR: Python {REQUIRED_MAJOR}.{REQUIRED_MINOR}+ is strictly required.")
    sys.exit(1)

WORKSPACE_ROOT = Path.cwd().resolve()

directories = [
    WORKSPACE_ROOT / "config",
    WORKSPACE_ROOT / "database",
    WORKSPACE_ROOT / "docs",
    WORKSPACE_ROOT / "logs",
    WORKSPACE_ROOT / "output" / "tables",
    WORKSPACE_ROOT / "output" / "figures",
    WORKSPACE_ROOT / "workspace",
    WORKSPACE_ROOT / "scripts" / "checks",
    WORKSPACE_ROOT / "scripts" / "sync",
    WORKSPACE_ROOT / "src" / "core",
    WORKSPACE_ROOT / "src" / "evidence",
    WORKSPACE_ROOT / "src" / "literature",
    WORKSPACE_ROOT / "src" / "dataset",
    WORKSPACE_ROOT / "src" / "analysis",
    WORKSPACE_ROOT / "src" / "writing",
    WORKSPACE_ROOT / "src" / "r_scripts",
    WORKSPACE_ROOT / "src" / "utils",
    WORKSPACE_ROOT / "tests",
    WORKSPACE_ROOT / "papers" / "manuscript",
    WORKSPACE_ROOT / "papers" / "review",
    WORKSPACE_ROOT / "papers" / "references_pdf",
    WORKSPACE_ROOT / "data" / "raw",
    WORKSPACE_ROOT / "data" / "interim",
    WORKSPACE_ROOT / "data" / "processed",
    WORKSPACE_ROOT / "handoff",
    WORKSPACE_ROOT / "rules",
    WORKSPACE_ROOT / "advisor",
]

for folder in directories:
    folder.mkdir(parents=True, exist_ok=True)

FILES_MANIFEST = {}

FILES_MANIFEST["config/settings.yaml"] = '''project:
  name: "Research-OS"
  version: "2.0.0"
  environment: "development"
database:
  filename: "research_os.db"
  timeout: 30.0
logging:
  level: "INFO"
  console_output: true
api:
  timeout: 60
'''

FILES_MANIFEST["config/datasource.yaml"] = '''datasources:
  un_comtrade:
    base_url: "https://comtradeapi.un.org/public/v1/preview/C/A/HS"
    rate_limit_per_minute: 10
  world_bank:
    base_url: "https://api.worldbank.org/v2"
'''

FILES_MANIFEST["config/logging.yaml"] = '''version: 1
disable_existing_loggers: false
formatters:
  standard:
    format: "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    datefmt: "%Y-%m-%d %H:%M:%S"
handlers:
  console:
    class: "logging.StreamHandler"
    level: "INFO"
    formatter: "standard"
    stream: "ext://sys.stdout"
  file:
    class: "logging.handlers.TimedRotatingFileHandler"
    level: "DEBUG"
    formatter: "standard"
    filename: "logs/research_os.log"
    when: "midnight"
    interval: 1
    backupCount: 30
    encoding: "utf-8"
loggers:
  research_os:
    handlers: ["console", "file"]
    level: "DEBUG"
    propagate: false
'''

FILES_MANIFEST["database/schema.sql"] = '''PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS project (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created_at TEXT DEFAULT (datetime(\'now\', \'utc\')),
    updated_at TEXT DEFAULT (datetime(\'now\', \'utc\'))
);

CREATE TABLE IF NOT EXISTS research_question (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    question TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT \'OPEN\',
    created_at TEXT DEFAULT (datetime(\'now\', \'utc\')),
    updated_at TEXT DEFAULT (datetime(\'now\', \'utc\')),
    FOREIGN KEY (project_id) REFERENCES project(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS literature (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    authors TEXT,
    venue TEXT,
    year INTEGER,
    doi TEXT,
    url TEXT,
    abstract TEXT,
    local_path TEXT,
    created_at TEXT DEFAULT (datetime(\'now\', \'utc\'))
);

CREATE TABLE IF NOT EXISTS dataset (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    source TEXT,
    version TEXT,
    local_path TEXT,
    description TEXT,
    created_at TEXT DEFAULT (datetime(\'now\', \'utc\'))
);

CREATE TABLE IF NOT EXISTS evidence (
    id TEXT PRIMARY KEY,
    question_id TEXT NOT NULL,
    source_type TEXT NOT NULL,
    source_id TEXT,
    content TEXT NOT NULL,
    reliability_score REAL DEFAULT 1.0,
    created_at TEXT DEFAULT (datetime(\'now\', \'utc\')),
    updated_at TEXT DEFAULT (datetime(\'now\', \'utc\')),
    FOREIGN KEY (question_id) REFERENCES research_question(id) ON DELETE CASCADE
);
'''

FILES_MANIFEST["src/core/exceptions.py"] = '''"""Platform exceptions for Research-OS architecture."""

class ResearchOSError(Exception):
    """Base exception class for all Research-OS framework errors."""
    pass

class ConfigurationError(ResearchOSError):
    """Raised when configuration loading, parsing, or structural validity fails."""
    pass

class DatabaseError(ResearchOSError):
    """Raised when local SQLite persistence operations encounter operational failures."""
    pass
'''

FILES_MANIFEST["src/core/paths.py"] = '''"""Centralized filesystem path configurations using pathlib."""

from pathlib import Path

WORKSPACE_ROOT = Path.cwd().resolve()

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
'''

FILES_MANIFEST["src/core/config.py"] = '''"""Thread-safe configuration manager implementation."""

from typing import Any, Dict, Optional
import yaml
from src.core.paths import SETTINGS_YAML, DATASOURCE_YAML, LOGGING_YAML
from src.core.exceptions import ConfigurationError

class ConfigManager:
    _instance: Optional["ConfigManager"] = None
    _initialized: bool = False

    def __new__(cls) -> "ConfigManager":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if self._initialized:
            return
        self._settings: Dict[str, Any] = {}
        self._datasource: Dict[str, Any] = {}
        self._logging: Dict[str, Any] = {}
        self.load_all()
        ConfigManager._initialized = True

    def load_all(self) -> None:
        self._settings = self._load_file(SETTINGS_YAML, "settings")
        self._datasource = self._load_file(DATASOURCE_YAML, "datasource")
        self._logging = self._load_file(LOGGING_YAML, "logging")

    def _load_file(self, path: Any, name: str) -> Dict[str, Any]:
        if not path.exists():
            return {}
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
                return data if isinstance(data, dict) else {}
        except Exception as e:
            raise ConfigurationError(f"Failed parsing file config content {name} at {path}: {e}") from e

    def get(self, key_path: str, default: Any = None) -> Any:
        parts = key_path.split(".")
        if not parts:
            return default
        current: Any = self._settings
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return default
        return current
'''

FILES_MANIFEST["src/core/database.py"] = '''"""SQLite interface manager for local research persistence."""

import sqlite3
from typing import Any, List, Dict, Optional, Tuple
from src.core.paths import DB_FILE, SCHEMA_SQL
from src.core.exceptions import DatabaseError

class Database:
    def __init__(self, db_path: Optional[Any] = None) -> None:
        self.db_path = str(db_path if db_path is not None else DB_FILE)
        self.connection: Optional[sqlite3.Connection] = None

    def connect(self) -> sqlite3.Connection:
        if self.connection is None:
            try:
                self.connection = sqlite3.connect(self.db_path, timeout=30.0)
                self.connection.execute("PRAGMA foreign_keys = ON;")
                self.connection.row_factory = sqlite3.Row
            except sqlite3.Error as e:
                raise DatabaseError(f"Database connectivity failed at {self.db_path}: {e}") from e
        return self.connection

    def close(self) -> None:
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def execute(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> sqlite3.Cursor:
        conn = self.connect()
        try:
            return conn.execute(query, params or ())
        except sqlite3.Error as e:
            raise DatabaseError(f"Database statement error: {e}")

    def fetch_all(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> List[Dict[str, Any]]:
        cursor = self.execute(query, params)
        return [dict(row) for row in cursor.fetchall()]
'''

package_inits = [
    "src/__init__.py", "src/core/__init__.py", "src/analysis/__init__.py",
    "src/dataset/__init__.py", "src/evidence/__init__.py", "src/literature/__init__.py",
    "src/writing/__init__.py", "src/utils/__init__.py"
]

for init_path in package_inits:
    FILES_MANIFEST[init_path] = '"""Package init marker."""\n'

def main():
    print("=== Research-OS Foundation Initialization ===")
    root = WORKSPACE_ROOT
    for rel_path, content in FILES_MANIFEST.items():
        file_path = root / rel_path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        if not file_path.exists() or file_path.stat().st_size == 0:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  + Created: {rel_path}")
        else:
            print(f"  . Exists:  {rel_path}")

    # Initialize sqlite db
    db_path = root / "database" / "research_os.db"
    schema_path = root / "database" / "schema.sql"
    try:
        conn = sqlite3.connect(str(db_path))
        with open(schema_path, "r", encoding="utf-8") as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()
        print(f"\n✅ Local SQLite database initialized at {db_path.relative_to(root)}")
    except Exception as e:
        print(f"⚠️  Database setup warning: {e}")

    print("\n🚀 Research-OS successfully provisioned.")

if __name__ == "__main__":
    main()
