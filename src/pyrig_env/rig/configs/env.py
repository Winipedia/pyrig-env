"""Configuration for the target project's `.env` file."""

from pathlib import Path
from typing import Any

from pyrig.rig.configs.base.config_file import DictConfigFile


class EnvConfigFile(DictConfigFile):
    """Config file manager for the target project's `.env` file.

    Only ever creates an empty `.env` file when one is missing; its content is
    never read or overwritten afterward, so users are free to populate and
    maintain secrets and local environment variables by hand. Excluded from
    version control so those secrets are never committed.
    """

    def _configs(self) -> dict[str, Any]:
        """Return an empty dict, since no `.env` content is required."""
        return {}

    def _dump(self, configs: dict[str, Any]) -> None:
        """Refuse to write non-empty content to `.env`; no-op for an empty dict.

        Args:
            configs: Configuration to write. Must be empty.

        Raises:
            ValueError: If `configs` is non-empty.
        """
        if not configs:
            return
        msg = f"""cannot dump to {self}"""
        raise ValueError(msg)

    def _load(self) -> dict[str, str | None]:
        """Refuse to load `.env` content.

        Raises:
            RuntimeError: Always.
        """
        msg = f"{self} should never be loaded."
        raise RuntimeError(msg)

    def extension(self) -> str:
        """Return `""`, since `.env` has no extension."""
        return ""

    def extension_separator(self) -> str:
        """Return `""`, so the stem is not followed by a trailing dot."""
        return ""

    def is_correct(self) -> bool:
        """Return whether `.env` exists, without loading its content."""
        return self.path().exists()

    def parent_path(self) -> Path:
        """Return the project root as the parent directory."""
        return Path()

    def stem(self) -> str:
        """Return `".env"`."""
        return ".env"

    def version_control_ignored(self) -> bool:
        """Return `True`; `.env` is always excluded from version control."""
        return True
