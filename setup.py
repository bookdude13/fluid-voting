# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='fvote',
    version='0.1.0',
    description='Fluid voting library',
    long_description=readme,
    author='Ryan Fredlund',
    author_email='rfredlund13@gmail.com',
    url='https://github.com/bookdude13/fluid-voting',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)