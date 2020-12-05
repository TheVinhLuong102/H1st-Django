import os
from pathlib import Path
from ruamel import yaml
import shutil


_H1ST_DJANGO_UTIL_CLI_STANDARD_FILES_DIR_PATH = \
    Path(__file__).parent / '_standard_files'

_H1ST_DJANGO_CONFIG_FILE_NAME = '.config.yml'

_MANAGE_PY_FILE_NAME = 'manage.py'
_MANAGE_PY_FILE_SRC_PATH = \
    _H1ST_DJANGO_UTIL_CLI_STANDARD_FILES_DIR_PATH / _MANAGE_PY_FILE_NAME

_ASGI_PY_FILE_NAME = 'asgi.py'
_ASGI_PY_FILE_SRC_PATH = \
    _H1ST_DJANGO_UTIL_CLI_STANDARD_FILES_DIR_PATH / _ASGI_PY_FILE_NAME

_WSGI_PY_FILE_NAME = 'wsgi.py'
_WSGI_PY_FILE_SRC_PATH = \
    _H1ST_DJANGO_UTIL_CLI_STANDARD_FILES_DIR_PATH / _WSGI_PY_FILE_NAME

_DAPHNE_PROCFILE_NAME = 'Procfile.Daphne'
_DAPHNE_PROCFILE_SRC_PATH = \
    _H1ST_DJANGO_UTIL_CLI_STANDARD_FILES_DIR_PATH / _DAPHNE_PROCFILE_NAME

_HYPERCORN_PROCFILE_NAME = 'Procfile.Hypercorn'
_HYPERCORN_PROCFILE_SRC_PATH = \
    _H1ST_DJANGO_UTIL_CLI_STANDARD_FILES_DIR_PATH / _HYPERCORN_PROCFILE_NAME

_UVICORN_PROCFILE_NAME = 'Procfile.Uvicorn'
_UVICORN_PROCFILE_SRC_PATH = \
    _H1ST_DJANGO_UTIL_CLI_STANDARD_FILES_DIR_PATH / _UVICORN_PROCFILE_NAME


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

    assert not os.path.exists(path=_H1ST_DJANGO_CONFIG_FILE_NAME)
    shutil.copyfile(
        src=h1st_django_config_file_path,
        dst=_H1ST_DJANGO_CONFIG_FILE_NAME)
    assert not os.path.exists(path=_MANAGE_PY_FILE_NAME)
    shutil.copyfile(
        src=_MANAGE_PY_FILE_SRC_PATH,
        dst=_MANAGE_PY_FILE_NAME)
    assert not os.path.exists(path=_ASGI_PY_FILE_NAME)
    shutil.copyfile(
        src=_ASGI_PY_FILE_SRC_PATH,
        dst=_ASGI_PY_FILE_NAME)
    assert not os.path.exists(path=_WSGI_PY_FILE_NAME)
    shutil.copyfile(
        src=_WSGI_PY_FILE_SRC_PATH,
        dst=_WSGI_PY_FILE_NAME)
    assert not os.path.exists(path=_DAPHNE_PROCFILE_NAME)
    shutil.copyfile(
        src=_DAPHNE_PROCFILE_SRC_PATH,
        dst=_DAPHNE_PROCFILE_NAME)
    assert not os.path.exists(path=_HYPERCORN_PROCFILE_NAME)
    shutil.copyfile(
        src=_HYPERCORN_PROCFILE_SRC_PATH,
        dst=_HYPERCORN_PROCFILE_NAME)
    assert not os.path.exists(path=_UVICORN_PROCFILE_NAME)
    shutil.copyfile(
        src=_UVICORN_PROCFILE_SRC_PATH,
        dst=_UVICORN_PROCFILE_NAME)

    os.system(command)

    os.remove(_H1ST_DJANGO_CONFIG_FILE_NAME)
    assert not os.path.exists(path=_H1ST_DJANGO_CONFIG_FILE_NAME)
    os.remove(_MANAGE_PY_FILE_NAME)
    assert not os.path.exists(path=_MANAGE_PY_FILE_NAME)
    os.remove(_ASGI_PY_FILE_NAME)
    assert not os.path.exists(path=_ASGI_PY_FILE_NAME)
    os.remove(_WSGI_PY_FILE_NAME)
    assert not os.path.exists(path=_WSGI_PY_FILE_NAME)
    os.remove(_DAPHNE_PROCFILE_NAME)
    assert not os.path.exists(path=_DAPHNE_PROCFILE_NAME)
    os.remove(_HYPERCORN_PROCFILE_NAME)
    assert not os.path.exists(path=_HYPERCORN_PROCFILE_NAME)
    os.remove(_UVICORN_PROCFILE_NAME)
    assert not os.path.exists(path=_UVICORN_PROCFILE_NAME)
