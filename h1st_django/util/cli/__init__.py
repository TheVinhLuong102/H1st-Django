import os
from pathlib import Path
from ruamel import yaml
import shutil


_H1ST_DJANGO_CREDS_FILE_NAME = '.creds.yml'
_H1ST_DJANGO_CREDS_FILE_PATH = Path(_H1ST_DJANGO_CREDS_FILE_NAME).resolve()


def run_command_with_substituted_creds_file(
        command: str,
        creds_file_path: str):
    creds_file_path = Path(creds_file_path).expanduser()

    creds = yaml.safe_load(stream=open(creds_file_path, 'r'))

    db_creds = creds['db']
    assert db_creds['host'] \
       and db_creds['user'] \
       and db_creds['password'] \
       and db_creds['db-name']

    _tmp_h1st_django_creds_file_path = \
        _H1ST_DJANGO_CREDS_FILE_PATH.with_suffix(
            _H1ST_DJANGO_CREDS_FILE_PATH.suffix + '.orig')
    assert not os.path.isfile(_tmp_h1st_django_creds_file_path)

    shutil.copyfile(
        src=_H1ST_DJANGO_CREDS_FILE_PATH,
        dst=_tmp_h1st_django_creds_file_path)
    assert os.path.isfile(_tmp_h1st_django_creds_file_path)

    shutil.copyfile(
        src=creds_file_path,
        dst=_H1ST_DJANGO_CREDS_FILE_PATH)

    os.system(command)

    shutil.copyfile(
        src=_tmp_h1st_django_creds_file_path,
        dst=_H1ST_DJANGO_CREDS_FILE_PATH)

    os.remove(_tmp_h1st_django_creds_file_path)
    assert not os.path.isfile(_tmp_h1st_django_creds_file_path)
