# -*- coding: UTF-8 -*-

'''
Module
    __init__.py
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
    Defines class GenLKM with attribute(s) and method(s).
    Generates LKM by templates and parameters.
'''

import sys
from typing import List, Dict
from os.path import dirname, realpath

try:
    from ats_utilities.pro_config import ProConfig
    from ats_utilities.pro_config.pro_name import ProName
    from ats_utilities.config_io.file_check import FileCheck
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from gen_kernel_module.lkm.read_template import ReadTemplate
    from gen_kernel_module.lkm.write_template import WriteTemplate
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


class GenLKM(FileCheck, ProConfig, ProName):
    '''
        Defines class GenLKM with attribute(s) and method(s).
        Generates LKM by templates and parameters.

        It defines:

            :attributes:
                | _GEN_VERBOSE - Console text indicator for process-phase.
                | _PRO_STRUCTURE - Project setup (templates, modules).
                | _reader - Reader API.
                | _writer - Writer API.
            :methods:
                | __init__ - Initials GenLKM constructor.
                | get_reader - Gets template reader.
                | get_writer - Gets template writer.
                | gen_module - Generates LKM.
    '''

    _GEN_VERBOSE: str = 'GEN_KERNEL_MODULE::LKM::GEN_LKM'
    _PRO_STRUCTURE: str = '/../conf/project.yaml'

    def __init__(self, verbose: bool = False) -> None:
        '''
            Initials GenLKM constructor.

            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        FileCheck.__init__(self, verbose)
        ProConfig.__init__(self, verbose)
        ProName.__init__(self, verbose)
        verbose_message(
            verbose, [f'{self._GEN_VERBOSE.lower()} init generator']
        )
        self._reader: ReadTemplate | None = ReadTemplate(verbose)
        self._writer: WriteTemplate | None = WriteTemplate(verbose)
        current_dir: str = dirname(realpath(__file__))
        pro_structure: str = f'{current_dir}{self._PRO_STRUCTURE}'
        self.check_path(pro_structure, verbose)
        self.check_mode('r', verbose)
        self.check_format(pro_structure, 'yaml', verbose)
        if self.is_file_ok():
            yml2obj: Yaml2Object | None = Yaml2Object(pro_structure)
            self.config = yml2obj.read_configuration()

    def get_reader(self) -> ReadTemplate | None:
        '''
            Gets template reader.

            :return: Template reader object | None
            :rtype: <ReadTemplate> | <NoneType>
            :exceptions: None
        '''
        return self._reader

    def get_writer(self) -> WriteTemplate | None:
        '''
            Gets template writer.

            :return: Template writer object | none
            :rtype: <WriteTemplate> | <NoneType
            :exceptions: None
        '''
        return self._writer

    def gen_module(
        self,
        lkm_name: str | None,
        lkm_type: str | None,
        verbose: bool = False
    ) -> bool:
        '''
            Generates LKM.

            :param lkm_name: Module name | None
            :type lkm_name: <str> | <NoneType>
            :param lkm_type: Model type | None
            :type lkm_type: <str> | <NoneType>
            :param verbose: Enable/Disable verbose option
            :type verbose: <bool>
            :return: True (success operation) | False
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSValueError
        '''
        error_msg: str | None = None
        error_id: int | None = None
        error_msg, error_id = self.check_params([
            ('str:lkm_name', lkm_name), ('str:lkm_type', lkm_type)
        ])
        if error_id == self.TYPE_ERROR:
            raise ATSTypeError(error_msg)
        if not bool(lkm_name):
            raise ATSValueError('missing LKM name')
        if not bool(lkm_type):
            raise ATSValueError('missing LKM type')
        status: bool = False
        verbose_message(
            verbose, [
                f'{self._GEN_VERBOSE.lower()}',
                'generate', lkm_type, 'form', lkm_name
            ]
        )
        if bool(self._reader) and bool(self.config):
            template_content: Dict[str, str] = self._reader.read(
                self.config, lkm_name, lkm_type, verbose
            )
            if bool(template_content) and bool(self._writer):
                status = self._writer.write(
                    template_content, lkm_name, verbose
                )
        return status
