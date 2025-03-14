# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion"
    # "swagger-ui-bundle>=0.0.2",
    # "requests"
]

setup(
    name=NAME,
    version=VERSION,
    description="Service Resource Manager Controller API",
    author_email="dlaskaratos@intracom-telecom.com",
    url="",
    keywords=["Swagger", "service resource manager API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    API exposed by π-edge for \&quot;PaaS &amp; Service Function\&quot; - based interaction with NFV MANO. 
    """
)
