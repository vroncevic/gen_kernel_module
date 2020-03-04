# -*- coding: UTF-8 -*-

"""
 Module
     read_template.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
     generate_kernel_module is free software: you can redistribute it and/or
     modify it under the terms of the GNU General Public License as published
     by the Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     generate_kernel_module is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define class ReadTemplate with attribute(s) and method(s).
     Read a template file (setup.template) and return a content.
"""

import sys
from inspect import stack
from os.path import isdir

try:
    from pathlib import Path

    from ats_utilities.config.yaml.yaml2object import Yaml2Object
    from ats_utilities.config.file_checking import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as error:
    MESSAGE = "\n{0}\n{1}\n".format(__file__, error)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

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
                CharDev - 0
                BlkDev - 1
                NetDev - 2
                VMADev - 3
                __MODULES - Mapped choice and template key
                __TEMPLATE_DIR - Template dir path
                __PROJECT - template/project structure
                __FORMAT - File format for template
                __template_dir - Absolute file path of template dir
                __pro_cfg - Yaml object for template/project description
            method:
                __init__ - Initial constructor
                get_template_directory - Getter for template directory object
                get_project_configurtion - Getter for project configuration
                get_check_cfg - Getter for status of project configuration
                read - Read a template and return a string representation
    """

    __slots__ = (
        'VERBOSE',
        'CharDev',
        'BlkDev',
        'NetDev',
        'VMADev',
        '__MODULES',
        '__TEMPLATE_DIR',
        '__PROJECT',
        '__FORMAT',
        '__check_cfg',
        '__template_dir',
        '__pro_cfg'
    )
    VERBOSE = 'GEN_KERNEL_MODULE::LKM::READ_TEMPLATE'
    CharDev, BlkDev, NetDev, VMADev = range(4)
    __MODULES = {
        CharDev: 'lkm_charachter_device',
        BlkDev: 'lkm_block_device',
        NetDev: 'lkm_network_interfaces',
        VMADev: 'lkm_vma'
    }
    __TEMPLATE_DIR = '/../../conf/template/'
    __PROJECT = 'project.yaml'
    __FORMAT = 'template'

    def __init__(self, verbose=False):
        """
            Setting template dir from configuration directory.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(ReadTemplate.VERBOSE, verbose, 'Initial reader')
        FileChecking.__init__(self, verbose=verbose)
        current_dir = Path(__file__).parent
        template_dir = "{0}{1}".format(
            current_dir, ReadTemplate.__TEMPLATE_DIR
        )
        check_template_dir = isdir(template_dir)
        self.__check_cfg = False
        if check_template_dir:
            self.__template_dir = template_dir
            pro = "{0}/../../conf/{1}".format(
                current_dir, ReadTemplate.__PROJECT
            )
            self.__pro_cfg = Yaml2Object(pro)
        else:
            self.__template_dir = None
            self.__pro_cfg = None

    def get_template_directory(self):
        """
            Getter for template directory object
            :return: Template directory
            :rtype: <str>
            :exceptions: None
        """
        return self.__template_dir

    def get_project_configurtion(self):
        """
            Getter for project configuration
            :return: Project configuration
            :rtype: <Yaml2Object>
            :exceptions: None
        """
        return self.__pro_cfg

    def get_check_cfg(self):
        """
            Getter for status of project configuration
            :return: Project configuration status
            :rtype: <bool>
            :exceptions: None
        """
        return self.__check_cfg

    def read(self, module_type, module_name, verbose=False):
        """
            Read template structure.
            :param module_type: Type of kernel module
            :type module_type: <int>
            :param module_name: Parameter module name
            :type module_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Template content for setup module | None
            :rtype: <str> | <NoneType>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func, setup_content = stack()[0][3], {}
        type_txt = 'First argument: expected module_type <int> object'
        type_msg = "{0} {1} {2}".format('def', func, type_txt)
        if module_type is None:
            raise ATSBadCallError(type_msg)
        if not isinstance(module_type, int):
            raise ATSTypeError(type_msg)
        verbose_message(ReadTemplate.VERBOSE, verbose, 'Loading templates')
        self.__check_cfg = all(
            [bool(self.__template_dir), bool(self.__pro_cfg)]
        )
        if self.__check_cfg:
            pro_cfg = self.__pro_cfg.read_configuration(verbose=verbose)
            for pro_sec in pro_cfg:
                pro_cfg[pro_sec] = pro_cfg[pro_sec].split(' ')
            for template in pro_cfg[ReadTemplate.__MODULES[module_type]]:
                template_file, template_file_exists = None, False
                template_file = "{0}{1}".format(self.__template_dir, template)
                template_file_exists = self.check_file(
                    file_path=template_file, verbose=verbose
                )
                if template_file_exists:
                    with open(template_file, 'r') as tmpl:
                        template_list = []
                        if 'Makefile.template' in template_file:
                            template_list.append('Makefile')
                        if 'lkm.template' in template_file:
                            template_list.append("{0}.c".format(module_name))
                        if 'test.template' in template_file:
                            template_list.append('main.c')
                        template_list.append(tmpl.read())
                        setup_content[template] = template_list
        return setup_content
