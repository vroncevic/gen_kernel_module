# -*- coding: UTF-8 -*-

'''
Module
    main.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Main entry point for Task Code Generator CLI.
'''

from __future__ import annotations

from sys import exit

from gen_kernel_module.engine import GenKernelModule
from gen_kernel_module.setup.factory import GenKernelModuleBundleFactory

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_kernel_module'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_kernel_module/blob/dev/LICENSE'
__version__ = '1.4.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


def main() -> bool:
    '''
        Bootstraps and runs the gen_kernel_module with required adapters.

        :return: True if successful, False otherwise.
        :exceptions: None
    '''
    gen_kernel_module: GenKernelModule = GenKernelModule(GenKernelModuleBundleFactory.create_bundle())

    return gen_kernel_module.process()


if __name__ == '__main__':
    '''
        Entry point for gen_kernel_module execution.

        :exit code: 0 if successful, 1 otherwise.
        :exceptions: None
    '''
    exit(0 if main() else 1)
