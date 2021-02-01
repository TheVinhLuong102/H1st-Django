import json
from setuptools import find_namespace_packages, setup


_METADATA_FILE_NAME = 'metadata.json'
_PACKAGE_NAMESPACE_NAME = 'h1st'
_REQUIREMENTS_FILE_NAME = 'requirements.txt'


_metadata = json.load(open(_METADATA_FILE_NAME))


setup(
    name=_metadata['PACKAGE'],
    version=_metadata['VERSION'],
    namespace_packages=[_PACKAGE_NAMESPACE_NAME],
    packages=find_namespace_packages(include=[f'{_PACKAGE_NAMESPACE_NAME}.*']),
    include_package_data=True,
    install_requires=[s
                      for s in {i.strip() for i in
                                open(_REQUIREMENTS_FILE_NAME).readlines()}
                      if not s.startswith('#')],
    scripts=['h1st/django/util/cli/h1st',
             'h1st/django/util/cli/aws-eb/h1st-aws',
             'h1st/django/util/cli/clone-template/h1st-clone',
             'h1st/django/util/cli/clone-template/h1st-templates'])
