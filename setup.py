import json
from setuptools import setup


_METADATA_FILE_NAME = 'metadata.json'
_PACKAGE_NAMESPACE_NAME = 'h1ai_django'
_REQUIREMENTS_FILE_NAME = 'requirements.txt'


_metadata = json.load(open(_METADATA_FILE_NAME, 'r'))


setup(
    name=_metadata['PACKAGE'],
    version=_metadata['VERSION'],
    namespace_packages=[_PACKAGE_NAMESPACE_NAME],
    # packages=find_namespace_packages(include=[f'{_PACKAGE_NAMESPACE_NAME}.*']),
    include_package_data=True,
    install_requires=[s
                      for s in {i.strip() for i in
                                open(_REQUIREMENTS_FILE_NAME).readlines()}
                      if not s.startswith('#')])
