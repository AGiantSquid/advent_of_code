#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='aoc_utils',
    version='1.0',
    description='Utilities to help with Advent of Code',
    packages=find_packages(where='src'),
    package_dir={'': 'src'}
)