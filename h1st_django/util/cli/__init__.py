import os
from pathlib import Path
from ruamel import yaml
import shutil


_H1ST_DJANGO_CONFIG_FILE_NAME = _H1ST_DJANGO_CONFIG_FILE_PATH = '.config.yml'


def run_command_with_config_file(
        command: str,
        h1st_django_config_file_path: str):
    h1st_django_config_file_path = \
        Path(h1st_django_config_file_path).expanduser()

    configs = yaml.safe_load(stream=open(h1st_django_config_file_path))

    db_creds = configs['db']
    assert db_creds['host'] \
       and db_creds['user'] \
       and db_creds['password'] \
       and db_creds['db-name']

    assert not os.path.exists(path=_H1ST_DJANGO_CONFIG_FILE_PATH)
    shutil.copyfile(
        src=h1st_django_config_file_path,
        dst=_H1ST_DJANGO_CONFIG_FILE_PATH)

    os.system(command)

    os.remove(_H1ST_DJANGO_CONFIG_FILE_PATH)
    assert not os.path.exists(path=_H1ST_DJANGO_CONFIG_FILE_PATH)
