PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS project (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created_at TEXT DEFAULT (datetime('now', 'utc')),
    updated_at TEXT DEFAULT (datetime('now', 'utc'))
);

CREATE TABLE IF NOT EXISTS research_question (
    id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    question TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'OPEN',
    created_at TEXT DEFAULT (datetime('now', 'utc')),
    updated_at TEXT DEFAULT (datetime('now', 'utc')),
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
    created_at TEXT DEFAULT (datetime('now', 'utc'))
);

CREATE TABLE IF NOT EXISTS dataset (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    source TEXT,
    version TEXT,
    local_path TEXT,
    description TEXT,
    created_at TEXT DEFAULT (datetime('now', 'utc'))
);

CREATE TABLE IF NOT EXISTS evidence (
    id TEXT PRIMARY KEY,
    question_id TEXT NOT NULL,
    source_type TEXT NOT NULL,
    source_id TEXT,
    content TEXT NOT NULL,
    reliability_score REAL DEFAULT 1.0,
    created_at TEXT DEFAULT (datetime('now', 'utc')),
    updated_at TEXT DEFAULT (datetime('now', 'utc')),
    FOREIGN KEY (question_id) REFERENCES research_question(id) ON DELETE CASCADE
);
