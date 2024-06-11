#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Module
    gen_kernel_module_run.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Main entry point for tool gen_kernel_module.
'''

import sys
from typing import List

try:
    from gen_kernel_module import GenKernelModule
except ImportError as ats_error_message:
    # Force close python ATS ##################################################
    sys.exit(f'\n{__file__}\n{ats_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_kernel_module'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_kernel_module/blob/dev/LICENSE'
__version__ = '1.3.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

if __name__ == '__main__':
    TOOL: GenKernelModule = GenKernelModule(verbose=False)
    TOOL.process(verbose=False)
