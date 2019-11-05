#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import sys
from setuptools import setup, find_packages

with open('README.md') as readme_file:   readme = readme_file.read()

def to_list(buffer): return list(filter(None, map(str.strip, buffer.splitlines())))

requirements = to_list("""
    click
""")

setup(
    name = 'data_splitter',
    version = '0.2.1',
    packages = find_packages(),
    install_requires = requirements,
    python_requires  = '>=3.6',

    description = "small command line program to split folder into train and test set",
    long_description = readme,
    long_description_content_type = 'text/markdown',
    keywords = 'deep learning, preprocessing',

    license = "Apache Software License 2.0",

    url = 'https://github.com/markkvdb/data-splitter',

    author = "Mark van der Broek",
    author_email = 'markvanderbroek@gmail.com',

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    entry_points={
        'console_scripts': [
            'data_splitter=data_splitter.data_splitter:data_splitter'
        ],
    },

    zip_safe = False,
)