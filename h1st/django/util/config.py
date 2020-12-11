import os
from pathlib import Path
from ruamel import yaml


_H1ST_DJANGO_CONFIG_FILE_NAME = '.config.yml'


def parse_config_file(path=_H1ST_DJANGO_CONFIG_FILE_NAME):
    if os.path.isfile(path):
        # parse whole YAML config file
        config = yaml.safe_load(stream=open(path))

        # read and adjust DB config section
        db_config = config.get('db')
        assert db_config, f'*** "db" KEY NOT FOUND IN {config} ***'

        db_host = db_config.get('host')
        assert db_host, f'*** "host" KEY NOT FOUND IN {db_config} ***'

        db_engine = db_config.get('engine')
        assert db_engine, f'*** "engine" KEY NOT FOUND IN {db_config} ***'
        assert db_engine in ('postgresql', 'mysql'), \
            ValueError(f'*** "{db_engine}" DATABASE ENGINE NOT SUPPORTED ***')

        db_user = db_config.get('user')
        assert db_user, f'*** "user" KEY NOT FOUND IN {db_config} ***'
        db_password = db_config.get('password')
        assert db_password, f'*** "password" KEY NOT FOUND IN {db_config} ***'

        db_name = db_config.get('name')
        assert db_name, f'*** "name" KEY NOT FOUND IN {db_config} ***'

        config['db'] = dict(HOST=db_host,
                            ENGINE=f'django.db.backends.{db_engine}',
                            PORT=5432 if db_engine == 'postgresql' else 3306,
                            USER=db_user,
                            PASSWORD=db_password,
                            NAME=db_name)

        return config

    else:
        # return blank config per template
        return yaml.safe_load(
                stream=open(Path(__file__).parent /
                            'cli' /
                            '_standard_files' /
                            f'{_H1ST_DJANGO_CONFIG_FILE_NAME}.template'))
