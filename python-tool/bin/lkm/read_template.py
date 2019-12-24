# -*- coding: UTF-8 -*-
# read_template.py
# Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# generate_kernel_module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# generate_kernel_module is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys
from inspect import stack
from os.path import isdir

try:
    from pathlib import Path

    from ats_utilities.config.file_checking import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ##################################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2018, Free software to use and distributed it.'
__credits__ = ['Vladimir Roncevic']
__license__ = 'GNU General Public License (GPL)'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReadTemplate(FileChecking):
    """
        Define class ReadTemplate with attribute(s) and method(s).
        Read a template file (setup.template) and return a content.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __TEMPLATE_DIR - Template dir path
                __TEMPLATES - Types of templates
                __FORMAT - File format for template
                __template_dir - Absolute file path of template dir
            method:
                __init__ - Initial constructor
                read - Read a template and return a string representation
    """

    __slots__ = (
        'VERBOSE',
        '__TEMPLATE_DIR',
        '__TEMPLATES',
        '__FORMAT',
        '__template_dir'
    )
    VERBOSE = 'GEN_KERNEL_MODULE::LKM::READ_TEMPLATE'
    __TEMPLATE_DIR = '/../../conf/template/'
    __TEMPLATES = {
        0:[
            'lkm_charachter_device/Makefile.template',
            'lkm_charachter_device/lkm.template',
            'lkm_charachter_device/test_lkm.template'
        ],
        1:[
            'lkm_block_device/Makefile.template',
            'lkm_block_device/lkm.template',
            'lkm_block_device/test_lkm.template'
        ],
        2:[
            'lkm_network_interfaces/Makefile.template',
            'lkm_network_interfaces/lkm.template',
            'lkm_network_interfaces/test_lkm.template'
        ],
        3:[
            'lkm_vma/Makefile.template',
            'lkm_vma/lkm.template',
            'lkm_vma/test_lkm.template'
        ]
    }
    __FORMAT = 'template'

    def __init__(self, verbose=False):
        """
            Setting template dir from configuration directory.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(
            ReadTemplate.VERBOSE, verbose, 'Initial reader'
        )
        FileChecking.__init__(self, verbose=verbose)
        current_dir = Path(__file__).parent
        template_dir = "{0}{1}".format(
            current_dir, ReadTemplate.__TEMPLATE_DIR
        )
        check_template_dir = isdir(template_dir)
        if check_template_dir:
            self.__template_dir = template_dir
        else:
            self.__template_dir = None

    def read(self, module_type, verbose=False):
        """
            Read template structure.
            :param module_type: Type of kernel module
            :type module_type: <int>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Template content for setup module | None
            :rtype: <str> | <NoneType>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func = stack()[0][3]
        type_txt = 'First argument: expected module_type <int> object'
        type_msg = "{0} {1} {2}".format('def', func, type_txt)
        if module_type is None:
            raise ATSBadCallError(type_msg)
        if not isinstance(module_type, int):
            raise ATSTypeError(type_msg)
        setup_content = {}
        verbose_message(ReadTemplate.VERBOSE, verbose, 'Loading templates')
        for template in ReadTemplate.__TEMPLATES[module_type]:
            template_file, template_file_exists = None, False
            template_file = "{0}{1}".format(self.__template_dir, template)
            template_file_exists = self.check_file(
                file_path=template_file, verbose=verbose
            )
            if template_file_exists:
                with open(template_file, 'r') as tmpl:
                    setup_content[template] = tmpl.read()
        return setup_content

