#!/usr/bin/env python
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

from __future__ import print_function
from typing import List
from os.path import abspath, dirname, join
from setuptools import setup

__author__: str = 'Vladimir Roncevic'
__copyright__: str = '(C) 2026, https://vroncevic.github.io/gen_kernel_module'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__: str = 'https://github.com/vroncevic/gen_kernel_module/blob/dev/LICENSE'
__version__: str = '1.3.9'
__maintainer__: str = 'Vladimir Roncevic'
__email__: str = 'elektron.ronca@gmail.com'
__status__: str = 'Updated'

TOOL_DIR = 'gen_kernel_module/'
CONF: str = 'conf'
TEMPLATE: str = 'conf/template'
LOG: str = 'log'
THIS_DIR: str = abspath(dirname(__file__))
long_description: str | None = None
with open(join(THIS_DIR, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()
PROGRAMMING_LANG: str = 'Programming Language :: Python ::'
VERSIONS: List[str] = ['3.10', '3.11', '3.12']
SUPPORTED_PY_VERSIONS: List[str] = [
    f'{PROGRAMMING_LANG} {VERSION}' for VERSION in VERSIONS
]
PYP_CLASSIFIERS: List[str] = SUPPORTED_PY_VERSIONS
setup(
    name='gen_kernel_module',
    version='1.3.9',
    description='Python App/Tool/Script Utilities',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_kernel_module/',
    license='GPL-3.0-or-later',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='tool, generator, kernel, unix, linux, os, lkm',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=['gen_kernel_module', 'gen_kernel_module.lkm'],
    install_requires=['ats-utilities'],
    package_data={
        'gen_kernel_module': [
            'py.typed',
            f'{CONF}/gen_kernel_module.logo',
            f'{CONF}/gen_kernel_module.cfg',
            f'{CONF}/gen_kernel_module_util.cfg',
            f'{CONF}/project.yaml',
            f'{TEMPLATE}/block/lkm.template',
            f'{TEMPLATE}/block/Makefile.template',
            f'{TEMPLATE}/block/test.template',
            f'{TEMPLATE}/char/lkm.template',
            f'{TEMPLATE}/char/Makefile.template',
            f'{TEMPLATE}/char/test.template',
            f'{TEMPLATE}/net/lkm.template',
            f'{TEMPLATE}/net/Makefile.template',
            f'{TEMPLATE}/net/test.template',
            f'{TEMPLATE}/vma/lkm.template',
            f'{TEMPLATE}/vma/Makefile.template',
            f'{TEMPLATE}/vma/test.template',
            f'{LOG}/gen_kernel_module.log'
        ]
    },
    data_files=[(
        '/usr/local/bin/', [
            f'{TOOL_DIR}run/gen_kernel_module_run.py'
        ]
    )]
)
