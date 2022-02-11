from setuptools import find_namespace_packages, setup
from pathlib import Path

ROOT = Path(__file__).parent.absolute()


def parse_requirements(filename):
    """
    load requirements from a pip requirements file
    """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


setup(
    name='baffi',
    version='0.0.1',
    description='This repository contains a phishing detection algorithm.',
    author='',
    packages=find_namespace_packages(include=['baffi.*'], exclude=['tests']),
    install_requires=[parse_requirements(ROOT / 'requirements.txt')],
    extras_require={
         'dev': parse_requirements(ROOT / 'dev-requirements.txt'),
         'docs': ['sphinx_rtd_theme', 'sphinx', 'myst_parser'],
    },
    tests_require=['pytest', 'pytest-cov', 'tox'])
