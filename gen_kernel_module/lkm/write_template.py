# -*- coding: UTF-8 -*-

'''
Module
    write_template.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_kernel_module is free software: you can redistribute it and/or
    modify it under the terms of the GNU General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_kernel_module is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class WriteTemplate with attribute(s) and method(s).
    Creates an API for write a template content with parameters to a file.
'''

import sys
from typing import List, Dict
from datetime import date
from os import getcwd, chmod, mkdir
from string import Template

try:
    from ats_utilities.config_io.file_check import FileCheck
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
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


class WriteTemplate(FileCheck):
    '''
        Defines class WriteTemplate with attribute(s) and method(s).
        Creates an API for write a template content with parameters to a file.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
            :methods:
                | __init__ - Initials WriteTemplate constructor.
                | write - write a template content with parameters to a file.
    '''

    _GEN_VERBOSE: str = 'GEN_KERNEL_MODULE::LKM::WRITE_TEMPLATE'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials WriteTemplate constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :excptions: None
        '''
        super().__init__(verbose)
        verbose_message(verbose, [f'{self._GEN_VERBOSE.lower()} init writer'])

    def write(
        self,
        template_content: Dict[str, str],
        lkm_name: str | None,
        verbose: bool = False
    ) -> bool:
        '''
            Write setup content to file.

            :param template_content: Template content
            :type template_content: <Dict[str, str]>
            :param lkm_name: LKM name | None
            :type lkm_name: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (success operation) | False
            :rtype: <bool>
            :exception: ATSTypeError | ATSValueError
        '''
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([
            ('dict:template_content', template_content),
            ('str:lkm_name', lkm_name)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(template_content):
            raise ATSValueError('missing model content')
        if not bool(lkm_name):
            raise ATSValueError('missing model name')
        all_stat: List[bool] = []
        num_of_modules: int = len(template_content)
        module_pro_dir: str = f'{getcwd()}/{lkm_name}/'
        mkdir(module_pro_dir)
        for module_name, module_content in template_content.items():
            module_path: str = f'{module_pro_dir}{module_name}'
            template: Template = Template(module_content)
            with open(module_path, 'w', encoding='utf-8') as module_file:
                module_file.write(template.substitute({
                    'LKM': lkm_name, 'YEAR': f'{date.today().year}'
                }))
                chmod(module_path, 0o644)
                self.check_path(module_path, verbose)
                self.check_mode('w', verbose)
                if 'makefile'.capitalize() in module_path:
                    self.check_format(
                        module_path, 'makefile', verbose
                    )
                else:
                    self.check_format(
                        module_path, module_path.split('.')[1], verbose
                    )
                if self.is_file_ok():
                    all_stat.append(True)
                else:
                    all_stat.append(False)
        return all([
            bool(all_stat), all(all_stat), num_of_modules == len(all_stat)
        ])
