# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.0.1',
    description='Mattermost(and Slack) incommig webhook client',
    long_description=readme,
    author='Naoki Someya',
    author_email='n.someya.ynu@gmail.com',
    url='https://github.com/n-someya/mattermost_client',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
