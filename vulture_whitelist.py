"""Explicit references for reviewed dead code false positives."""

from pyrig.rig.configs.base.config_file import ConfigFile

from pyrig_env.rig.configs.env import EnvConfigFile

_CONFIG_FILE_OVERRIDES = (
    ConfigFile._configs,
    ConfigFile._dump,
    ConfigFile._load,
    ConfigFile.extension,
    ConfigFile.extension_separator,
    ConfigFile.is_correct,
    ConfigFile.parent_path,
    ConfigFile.stem,
    ConfigFile.version_control_ignored,
)
_CONFIG_FILES = (EnvConfigFile,)
