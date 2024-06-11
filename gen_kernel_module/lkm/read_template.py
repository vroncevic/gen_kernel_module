# -*- coding: UTF-8 -*-

'''
Module
    read_template.py
Copyright
    Copyright (C) 2017 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_kernel_module is free software: you can redistribute it and/or
    modify it under the terms of the GNU General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_kernel_module is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines class ReadTemplate with attribute(s) and method(s).
    Creates an API for reading a LKM template.
'''

import sys
from typing import Any, List, Dict
from os.path import dirname, realpath

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


class ReadTemplate(FileCheck):
    '''
        Defines class ReadTemplate with attribute(s) and method(s).
        Creates an API for reading a LKM template.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _TEMPLATE_DIR - Prefix path to templates.
            :methods:
                | __init__ - Initials ReadTemplate constructor.
                | read - Reads a template.
    '''

    _GEN_VERBOSE: str = 'GEN_KERNEL_MODULE::LKM::READ_TEMPLATE'
    _TEMPLATE_DIR: str = '/../conf/template/'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials ReadTemplate constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        super().__init__(verbose)
        verbose_message(verbose, [f'{self._GEN_VERBOSE.lower()} init reader'])

    def read(
        self,
        config: Dict[Any, Any],
        lkm_name: str | None,
        lkm_type: str | None,
        verbose: bool = False
    ) -> Dict[str, str]:
        '''
            Reads a template.

            :param config: LKM configuration
            :type config: <Dict[Any, Any]>
            :param lkm_type: LKM type | None
            :type lkm_type: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: Loaded templates
            :rtype: <Dict[str, str]>
            :exceptions: ATSTypeError | ATSValueError
        '''
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([
            ('dict:config', config), ('str:lkm_type', lkm_type)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(config):
            raise ATSValueError('missing LKM templates')
        if not bool(lkm_type):
            raise ATSValueError('missing LKM type')
        current_dir: str = dirname(realpath(__file__))
        pro_structure: str = f'{current_dir}{self._TEMPLATE_DIR}'
        template_dir: str = f'{pro_structure}{lkm_type}/'
        template_content: Dict[str, str] = {}
        templates: List[str] = []
        index: int = -1
        if lkm_type in config['modules'][0]:
            index = 0
        elif lkm_type in config['modules'][1]:
            index = 1
        elif lkm_type in config['modules'][2]:
            index = 2
        else:
            return template_content
        templates = config['modules'][index][lkm_type][0]['templates']
        for template in templates:
            template_file: str = f'{template_dir}{template}'
            with open(template_file, 'r', encoding='utf-8') as module_file:
                module_key: str | None = None
                if 'lkm' in template_file:
                    module_key = f'{lkm_name}.c'
                if 'Makefile' in template_file:
                    module_key = 'Makefile'
                if 'test' in template_file:
                    module_key = 'main.c'
                if not module_key:
                    raise ATSValueError('corrupted project structure')
                template_content[module_key] = module_file.read()
        verbose_message(
            verbose, [f'{self._GEN_VERBOSE.lower()} {template_content}']
        )
        return template_content
