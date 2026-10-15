"""Thread-safe configuration manager implementation."""

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
