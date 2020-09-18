#!/usr/bin/env python
from setuptools import setup

setup(
    name='trades',
    version='0.0.1',
    author='Wasim Akram Khan',
    keywords='open-source, python, project_setup',
    description='A sample setup for a python project.',
    packages=['trades', 'usage', 'benchmark', 'tests'],
    license='MIT License ',
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    project_urls={
        "Source Code": "https://github.com/wasimusu/trades",
    },
    url="https://github.com/wasimusu/trades",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.7",
    ]
)
