from setuptools import setup, find_packages

PACKAGE_NAME = 'algoritmos'
VERSION='0.1'
DESCRIPTION='Algoritmos de programación'

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
)