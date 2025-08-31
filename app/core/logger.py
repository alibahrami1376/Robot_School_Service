
# Standard library
import json
from logging import (
    CRITICAL, DEBUG, ERROR, INFO, NOTSET, WARNING,
    Formatter, Handler, Logger, StreamHandler, getLogger
)
from logging.handlers import RotatingFileHandler
from typing import Any, Optional

# Third-party
import logfire
from logfire import Logfire, LogfireLoggingHandler

# Local application
# e.g., from app.schema.logger import LogSchema


class LogService:
    """
    Central logging service.

    Features:
        - Configurable via environment variables:
            LOG_LEVEL (default: INFO)
            LOG_DIR   (default: ./logs)
            LOGFIRE_TOKEN (optional)

        - Provides:
            * create_logger_root(name, level)
            * create_console_handler(...)
            * create_rotating_file_handler(...)
            * create_logfire_handler(token)
            * log_json(level, **fields)
            * (future) get_logger(name)
    """

    _configured: bool = False
    _logfire: Optional[Logfire] = None
    _logfire_handler: Optional[Handler] = None

    _root: Optional[Logger] = getLogger()
    _ch: Optional[Handler] = None
    _fh: Optional[Handler] = None

    _format = (
        "%(asctime)s | %(levelname)s | %(processName)s[%(process)d] | "
        "%(threadName)s[%(thread)d] | %(filename)s:%(lineno)d - "
        "%(funcName)s() | %(message)s"
    )
    _datefmt = "%Y-%m-%d %H:%M:%S"

    _level_map: dict[str, int] = {
        "CRITICAL": CRITICAL,
        "ERROR": ERROR,
        "WARNING": WARNING,
        "INFO": INFO,
        "DEBUG": DEBUG,
        "NOTSET": NOTSET,
    }

    # ---------------------------
    # Logger Creation
    # ---------------------------

    @classmethod
    def create_logger_root(cls, name_logger: Optional[str] = None, level: str = "DEBUG") -> bool:
        """Create root logger with given name and level."""
        try:
            _level = cls._level_map.get(level.upper(), INFO)
            cls._root = getLogger(name_logger)
            cls._root.setLevel(_level)
            return True
        except Exception as e:
            print(e)
            return False

    @classmethod
    def create_console_handler(
        cls,
        level: str = "DEBUG",
        fmt: str = "%(message)s",
        datefmt: str = "%Y-%m-%d %H:%M:%S"
    ) -> None:
        """Attach console handler to root logger."""
        try:
            cls._ch = StreamHandler()
            cls._ch.setLevel(cls._level_map.get(level.upper(), INFO))
            cls._ch.setFormatter(Formatter(fmt, datefmt=datefmt))
            if cls._root:
                cls._root.addHandler(cls._ch)
        except Exception as e:
            if cls._root:
                cls._root.warning("Failed to configure console handler: %s", e)

    @classmethod
    def create_rotating_file_handler( 
        cls,
        level: str = "DEBUG",
        filename: str = "test.log",
        max_bytes: int = 5_000_000,
        backup_count: int = 3,
        encoding: str = "utf-8",
        fmt: str = "%(message)s",
        datefmt: str = "%Y-%m-%d %H:%M:%S"
    ) -> None:
        """Attach rotating file handler to root logger."""
        try:
            cls._fh = RotatingFileHandler(
                filename=filename,
                maxBytes=max_bytes,
                backupCount=backup_count,
                encoding=encoding
            )
            cls._fh.setLevel(cls._level_map.get(level.upper(), INFO))
            cls._fh.setFormatter(Formatter(fmt, datefmt=datefmt))
            if cls._root:
                cls._root.addHandler(cls._fh)
        except Exception as e:
            if cls._root:
                cls._root.warning("Failed to configure rotating file handler: %s", e)

    @classmethod
    def create_logfire_handler(cls, token: str) -> None:
        """Attach Logfire handler if token is provided."""
        if token and logfire is not None:
            try:
                cls._logfire = logfire.configure(token=token)
                cls._logfire_handler = LogfireLoggingHandler()
                if cls._root:
                    cls._root.addHandler(cls._logfire_handler)
                    cls._root.info("Logfire configured")
            except Exception as e:
                if cls._root:
                    cls._root.warning("Failed to configure logfire: %s", e)

    # ---------------------------
    # Logging helpers
    # ---------------------------

    @classmethod
    def log_json(cls, level: str, **fields: Any) -> None:
        """Log a structured JSON payload at the given level."""
        payload = json.dumps(fields, ensure_ascii=False, default=str)
        level = level.upper()

        if cls._root is None:
            return

        match level:
            case "DEBUG":
                cls._root.debug(payload)
            case "INFO":
                cls._root.info(payload)
            case "WARNING":
                cls._root.warning(payload)
            case "ERROR":
                cls._root.error(payload)
            case "CRITICAL":
                cls._root.critical(payload)
            case _:
                cls._root.info(payload)  # fallback
    
    
    @classmethod
    def configure(
        cls,
        name_logger: str = "root",
        level_root: str = "DEBUG",
        console_level: str = "DEBUG",
        file_level: str = "DEBUG",
        logfire_token: Optional[str] = None,
        filename: str = "app.log",
        max_bytes: int = 5_000_000,
        backup_count: int = 5,
    ) -> None:
        """
        Configure logging system (only once).
        Includes:
        - Root logger
        - Console handler
        - Rotating file handler
        - Optional Logfire handler
        """

        if cls._configured:
            return

        try:
            # root logger
            cls.create_logger_root(name_logger=name_logger, level=level_root)
            assert cls._root is not None
            # console handler
            cls.create_console_handler(level=console_level)

            # file handler
            cls.create_rotating_file_handler(
                level=file_level,
                filename=filename,
                max_bytes=max_bytes,
                backup_count=backup_count,
            )

            # logfire handler (اختیاری)
            if logfire_token:
                cls.create_logfire_handler(token=logfire_token)

            cls._configured = True

            if cls._root is not None:
                cls._root.info("Logger configured successfully")

        except Exception as e:
            fallback_logger = getLogger("log_service_fallback")
            if not fallback_logger.handlers:
                handler = StreamHandler()
                handler.setFormatter(Formatter("[FALLBACK] %(asctime)s | %(levelname)s | %(message)s"))
                fallback_logger.addHandler(handler)
            fallback_logger.error("Logger configuration failed: %s", e)

    @classmethod
    def get_logger(cls, name: Optional[str] = None) -> Logger:
        if not cls._configured:
            cls.configure()
        return getLogger(name)



LogService.configure(logfire_token="pylf_v1_us_8cLwbzxN62g6flv9Nb6PnhMTjChKkJtK81zRBH9qQ2CF")