#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
 Module
     setup.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
     gen_kernel_module is free software: you can redistribute it and/or modify it
     under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     gen_kernel_module is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define setup for gen_kernel_module package.
"""

from os.path import abspath, dirname, join
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.1.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

THIS_DIR, LONG_DESCRIPTION = abspath(dirname(__file__)), None
with open(join(THIS_DIR, 'README.md')) as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name='gen_kernel_module',
    version='1.1.0',
    description='Python App/Tool/Script Utilities',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_kernel_module/',
    license='GPL 2018 Free software to use and distributed it.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords='kernel, unix, linux, generator',
    platforms='POSIX',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)'
    ],
    packages=['gen_kernel_module', 'gen_kernel_module.lkm'],
    install_requires=['ats-utilities'],
    data_files=[
        ('/usr/local/bin/', ['gen_kernel_module/run/gen_kernel_module_run.py']),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/',
            ['gen_kernel_module/conf/gen_kernel_module.cfg']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/',
            ['gen_kernel_module/conf/gen_kernel_module_util.cfg']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/',
            ['gen_kernel_module/conf/project.yaml']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_vma/',
            ['gen_kernel_module/conf/template/lkm_vma/Makefile.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_vma/',
            ['gen_kernel_module/conf/template/lkm_vma/test.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_vma/',
            ['gen_kernel_module/conf/template/lkm_vma/lkm.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_charachter_device/',
            ['gen_kernel_module/conf/template/lkm_charachter_device/Makefile.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_charachter_device/',
            ['gen_kernel_module/conf/template/lkm_charachter_device/test.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_charachter_device/',
            ['gen_kernel_module/conf/template/lkm_charachter_device/lkm.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_block_device/',
            ['gen_kernel_module/conf/template/lkm_block_device/Makefile.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_block_device/',
            ['gen_kernel_module/conf/template/lkm_block_device/test.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_block_device/',
            ['gen_kernel_module/conf/template/lkm_block_device/lkm.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_network_interfaces/',
            ['gen_kernel_module/conf/template/lkm_network_interfaces/Makefile.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_network_interfaces/',
            ['gen_kernel_module/conf/template/lkm_network_interfaces/test.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_kernel_module/conf/template/lkm_network_interfaces/',
            ['gen_kernel_module/conf/template/lkm_network_interfaces/lkm.template']
        ),
        (
            '/usr/local/lib/python2.7/dist-packages/gen_kernel_module/log/',
            ['gen_kernel_module/log/gen_kernel_module.log']
        )
    ]
)
