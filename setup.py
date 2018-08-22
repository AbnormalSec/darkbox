#!/usr/bin/env python

from setuptools import setup
from darkbox.darkbox import __version__

setup(
    name='darkbox',
    packages=['darkbox', 'darkbox.commands', 'darkbox.static'],
    version=__version__,
    description='Portable all-in-one cross-platform toolkit.',
    license='WTFPL',
    url='https://github.com/AbnormalSec/darkbox',
    author='AbnormalSec',
    author_email='vesche@protonmail.com',
    entry_points={
        'console_scripts': [
            'darkbox = darkbox.darkbox:main',
        ]
    },
    # install_requires=[],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Information Technology",
        "License :: Public Domain",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Security"
    ]
)
