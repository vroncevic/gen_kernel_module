# -*- coding: UTF-8 -*-

'''
Module
    setup.py
Copyright
    Copyright (C) 2017 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_kernel_module is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_kernel_module is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines setup for tool gen_kernel_module.
'''

from __future__ import annotations

from os import walk
from os.path import abspath, dirname, join, relpath
from setuptools import setup, find_packages

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_kernel_module'
__credits__: list[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_kernel_module/blob/dev/LICENSE'
__version__: str = '1.4.0'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

THIS_DIR: str = abspath(dirname(__file__))
long_description: str | None = None

with open(join(THIS_DIR, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()

PROGRAMMING_LANG: str = 'Programming Language :: Python ::'
VERSIONS: list[str] = ['3.12', '3.13', '3.14']
SUPPORTED_PY_VERSIONS: list[str] = [f'{PROGRAMMING_LANG} {VERSION}' for VERSION in VERSIONS]
PYP_CLASSIFIERS: list[str] = SUPPORTED_PY_VERSIONS


def find_package_data(pkg: str) -> list[str]:
    '''
        Finds all files in package to include in package_data.

        :param pkg: Package folder name.
        :return: List of package files relative to the package folder.
        :exceptions: None.
    '''
    package_data: list[str] = []

    for root, dirs, files in walk(pkg):
        dirs[:] = [d for d in dirs if d != '__pycache__']

        for file in files:
            if file.endswith('.pyc') or file == '.editorconfig':
                continue

            full_path: str = join(root, file)
            rel_path: str = relpath(full_path, pkg)
            package_data.append(rel_path)

    return package_data

setup(
    name='gen_kernel_module',
    version='1.4.0',
    description='Generating kernel module project',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_kernel_module/',
    license='GPL-3.0-or-later',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='Unix, Linux, Development, Kernel, LKM, Driver, generator',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=find_packages(exclude=['tests', 'tests.*', '*.*.pyc', '*.pyo']),
    install_requires=['ats-utilities'],
    package_data={'gen_kernel_module': find_package_data('gen_kernel_module')}
)
