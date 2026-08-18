# -*- coding: UTF-8 -*-

'''
Module
    bundle.py
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
    Defines the gen_kernel_module bundle.
'''

from __future__ import annotations

from dataclasses import dataclass

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.utils.reflection import instance_to_dict

from gen_kernel_module.core.service.iservice import IService
from gen_kernel_module.core.service.isubprocessor import ISubProcessor
from gen_kernel_module.infrastructure.cli.icli import ICLI

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_kernel_module'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_kernel_module/blob/dev/LICENSE'
__version__ = '1.4.1'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@dataclass(slots=True, frozen=True, kw_only=True)
class GenKernelModuleBundle:
    '''
        GenKernelModule bundle holding the components of the gen_kernel_module.

        It defines:

            :attributes:
                | base - The base bundle with the base components.
                | service - The service orchestrating the gen_kernel_module's execution.
                | subprocessor - The adapter executing the gen_kernel_module's sub-processes.
                | cli - The command-line interface adapter.
            :methods:
                | to_dict - Converts the gen_kernel_module bundle to a dictionary.
    '''

    base: BaseBundle
    service: IService
    subprocessor: ISubProcessor
    cli: ICLI

    def to_dict(self) -> dict[str, object]:
        '''
            Converts the gen_kernel_module bundle to a dictionary.

            :return: Dictionary representation of the gen_kernel_module bundle.
            :exceptions: None.
        '''
        return instance_to_dict(self)
