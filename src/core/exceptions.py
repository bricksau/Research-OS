"""Platform exceptions for Research-OS architecture."""

class ResearchOSError(Exception):
    """Base exception class for all Research-OS framework errors."""
    pass

class ConfigurationError(ResearchOSError):
    """Raised when configuration loading, parsing, or structural validity fails."""
    pass

class DatabaseError(ResearchOSError):
    """Raised when local SQLite persistence operations encounter operational failures."""
    pass
