import json
from pathlib import Path

from loguru import logger

_config_data = None
_CONFIG_FILE_PATH = Path("./data/configs/configs.json")

default_config = {
    "app": {
        "name": "FastAPI App Template",
        "host": "0.0.0.0",
        "port": 8080,
    },
    "settings": {
        "log_dir": "./data/logs",
    },
}


def _get_settings():
    global _config_data
    if _config_data is None:
        _config_data = _Settings()
    return _config_data


class _Settings:
    def __init__(self) -> None:
        # If custom config exists, use it. Otherwise, create default config and use it.
        self._initialize_configs()

        # Load configurations from JSON file
        with open(_CONFIG_FILE_PATH, encoding="utf-8") as file:
            self.configs = json.load(file)

        # Application settings
        self.app_name: str = self.configs["app"]["name"]
        self.app_host: str = self.configs["app"]["host"]
        self.app_port: int = self.configs["app"]["port"]

        # Other settings
        self.log_dir: Path = Path(self.configs["settings"]["log_dir"])

    def _initialize_configs(self) -> None:
        # If config file does not exist, create a default one.
        if not _CONFIG_FILE_PATH.exists():
            _CONFIG_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
            with open(_CONFIG_FILE_PATH, "w", encoding="utf-8") as f:
                json.dump(default_config, f, ensure_ascii=False, indent=4)
            logger.info(
                "configs.configs.py - Settings._initialize_configs(): Created configs.json.defautlt"
            )
