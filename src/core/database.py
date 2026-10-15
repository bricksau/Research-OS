"""SQLite interface manager for local research persistence."""

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
