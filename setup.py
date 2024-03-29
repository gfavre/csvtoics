#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['ics', 'click']

setup_requirements = ['py2app']

test_requirements = [ ]
OPTIONS = {'argv_emulation': True,}
setup(
    app=['csvtoics/cli.py'],
    author="Gregory Favre",
    author_email='greg@beyondthewall.ch',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="CSV to ICS export",
    entry_points={
        'console_scripts': [
            'csvtoics=csvtoics.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='csvtoics',
    name='csvtoics',
    options={'py2app': OPTIONS},
    packages=find_packages(include=['csvtoics']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/gfavre/csvtoics',
    version='0.1.0',
    zip_safe=False,
)
