#!/usr/bin/env python

import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='darkbox',
    packages=[
        'darkbox',
        'darkbox.commands',
        'darkbox.static',
        'darkbox.util',
    ],
    version='0.1.0',
    description='Portable, all-in-one, cross-platform toolkit.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='WTFPL',
    url='https://github.com/AbnormalSec/darkbox',
    author='AbnormalSec',
    author_email='vesche@protonmail.com',
    entry_points={
        'console_scripts': [
            'darkbox = darkbox.darkbox:main',
        ]
    },
    install_requires=[
        'distro',
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Information Technology",
        "License :: Public Domain",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Topic :: Security"
    ]
)
