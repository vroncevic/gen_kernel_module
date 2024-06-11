# -*- coding: UTF-8 -*-

'''
Module
    write_template_test.py
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
    Defines class WriteTemplateTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of WriteTemplate.
Execute
    python3 -m unittest -v write_template_test
'''

import sys
from typing import List, Dict
from os.path import dirname, realpath
from unittest import TestCase, main

try:
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from gen_kernel_module.lkm.read_template import ReadTemplate
    from gen_kernel_module.lkm.write_template import WriteTemplate
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_kernel_module'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_kernel_module/blob/dev/LICENSE'
__version__ = '1.3.7'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplateTestCase(TestCase):
    '''
        Defines class WriteTemplateTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of WriteTemplate.
        WriteTemplate unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_write_template_create - Test write templates create.
                | test_write_template_empty - Test write templates empty.
                | test_write_template_none - Test write templates None.
                | test_write_name_empty - Test write name empty.
                | test_write_name_none - Test write name None.
                | test_write_template - Test write templates.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_write_template_create(self) -> None:
        '''Test write templates create'''
        template_write = WriteTemplate()
        self.assertIsNotNone(template_write)

    def test_write_template_empty(self) -> None:
        '''Test write templates empty'''
        template_write = WriteTemplate()
        content: Dict[str, str] = {}
        with self.assertRaises(ATSValueError):
            self.assertFalse(template_write.write(content, 'empty_simple'))

    def test_write_template_none(self) -> None:
        '''Test write templates None'''
        template_write = WriteTemplate()
        with self.assertRaises(ATSTypeError):
            self.assertFalse(
                template_write.write(None, 'none_simple')  # type: ignore
            )

    def test_write_name_empty(self) -> None:
        '''Test write name empty'''
        template_write = WriteTemplate()
        template_read = ReadTemplate()
        current_dir: str = dirname(realpath(__file__))
        pro: str = '../gen_kernel_module/conf/project.yaml'
        pro_structure: str = f'{current_dir}/{pro}'
        yml2obj: Yaml2Object | None = Yaml2Object(pro_structure)
        content: Dict[str, str] = template_read.read(
            yml2obj.read_configuration(), 'simple_write', 'char'
        )
        with self.assertRaises(ATSValueError):
            self.assertFalse(template_write.write(content, ''))

    def test_write_name_none(self) -> None:
        '''Test write name None'''
        template_write = WriteTemplate()
        template_read = ReadTemplate()
        current_dir: str = dirname(realpath(__file__))
        pro: str = '../gen_kernel_module/conf/project.yaml'
        pro_structure: str = f'{current_dir}/{pro}'
        yml2obj: Yaml2Object | None = Yaml2Object(pro_structure)
        content: Dict[str, str] = template_read.read(
            yml2obj.read_configuration(), 'simple_write', 'char'
        )
        with self.assertRaises(ATSTypeError):
            template_write.write(content, None)

    def test_write_template(self) -> None:
        '''Test write templates'''
        template_read = ReadTemplate()
        current_dir: str = dirname(realpath(__file__))
        pro: str = '../gen_kernel_module/conf/project.yaml'
        pro_structure: str = f'{current_dir}/{pro}'
        yml2obj: Yaml2Object | None = Yaml2Object(pro_structure)
        content: Dict[str, str] = template_read.read(
            yml2obj.read_configuration(), 'simple_write', 'char'
        )
        template_write = WriteTemplate()
        self.assertTrue(template_write.write(content, 'simple_write'))


if __name__ == '__main__':
    main()
