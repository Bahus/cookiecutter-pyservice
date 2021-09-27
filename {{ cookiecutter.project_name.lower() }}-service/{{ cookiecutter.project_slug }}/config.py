import sys
from pathlib import Path

from dynaconf import LazySettings

IS_COMMAND = not {Path(p).name for p in sys.argv} & {'uwsgi'}

settings = LazySettings(
    ENVVAR_PREFIX_FOR_DYNACONF='ACME',
    SETTINGS_FILE_FOR_DYNACONF='settings.yaml;settings.local.yaml',
    MERGE_ENABLED_FOR_DYNACONF=True,
    SILENT_ERRORS_FOR_DYNACONF=False,
)
settings.configure()

TRUSTED_PROXIES_NUMBER = settings['trusted_proxies_number']
