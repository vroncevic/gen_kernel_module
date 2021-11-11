# -*- coding: UTF-8 -*-

'''
 Module
     read_template.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class ReadTemplate with attribute(s) and method(s).
     Defined API for reading templates for LKM.
'''

import sys
from os.path import isdir

try:
    from pathlib import Path
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.error import error_message
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2017, https://vroncevic.github.io/gen_kernel_module'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_kernel_module/blob/dev/LICENSE'
__version__ = '1.2.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReadTemplate(FileChecking):
    '''
        Defined class ReadTemplate with attribute(s) and method(s).
        Defined API for reading templates for LKM.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | TEMPLATE_DIR - template dir path.
                | ROOT_KEY - root key for template.
                | FORMAT - format extension for templates.
                | MAKEFILE - makefile template.
                | LKM - lkm template.
                | TEST - test template.
                | MAKEFILE_MOD - makefile module.
                | LKM_MOD - lkm module.
                | TEST_MOD - test module.
            :methods:
                | __init__ - initial constructor.
                | read - read a templates and return a string representations.
                | __str__ - dunder method for ReadTemplate.
    '''

    GEN_VERBOSE = 'GEN_KERNEL_MODULE::LKM::READ_TEMPLATE'
    TEMPLATE_DIR = '/../conf/template/'
    ROOT_KEY, FORMAT = 'templates', 'template'
    MAKEFILE, LKM, TEST = 'Makefile.template', 'lkm.template', 'test.template'
    MAKEFILE_MOD, LKM_MOD, TEST_MOD = 'Makefile', '{0}.c', 'main.c'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(ReadTemplate.GEN_VERBOSE, verbose, 'init reader')

    def read(self, module_type, module_name, verbose=False):
        '''
            Read template structure.

            :param module_type: type of kernel module with templates.
            :type module_type: <dict>
            :param module_name: parameter module name.
            :type module_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: template list for generation, True | empty list, False.
            :rtype: <list>, <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('dict:module_type', module_type),
            ('str:module_name', module_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        lkm_type = module_type.keys()[0]
        template_dir = '{0}{1}{2}/'.format(
            Path(__file__).parent, ReadTemplate.TEMPLATE_DIR, lkm_type
        )
        template_list, status = [], False
        if isdir(template_dir):
            templates = module_type[lkm_type][1][ReadTemplate.ROOT_KEY]
            expected_num_of_modules = len(templates)
            for template in templates:
                template_file = '{0}{1}'.format(template_dir, template)
                self.check_path(file_path=template_file, verbose=verbose)
                self.check_mode(file_mode='r', verbose=verbose)
                self.check_format(
                    file_path=template_file, file_format=ReadTemplate.FORMAT,
                    verbose=verbose
                )
                if self.is_file_ok():
                    with open(template_file, 'r') as template_object:
                        template_content = template_object.read()
                        if ReadTemplate.MAKEFILE in template_file:
                            template_list.append({
                                lkm_type: [
                                    '{0}/{1}'.format(
                                        module_name,
                                        ReadTemplate.MAKEFILE_MOD
                                    ),
                                    template_content
                                ]
                            })
                        if ReadTemplate.LKM in template_file:
                            template_list.append({
                                lkm_type: [
                                    '{0}/{1}'.format(
                                        module_name,
                                        ReadTemplate.LKM_MOD.format(
                                            module_name
                                        )
                                    ),
                                    template_content
                                ]
                            })
                        if ReadTemplate.TEST in template_file:
                            template_list.append({
                                lkm_type: [
                                    '{0}/{1}'.format(
                                        module_name, ReadTemplate.TEST_MOD
                                    ),
                                    template_content
                                ]
                            })
                        verbose_message(
                            ReadTemplate.GEN_VERBOSE, verbose,
                            'loaded template', template_file
                        )
                    if len(template_list) == expected_num_of_modules:
                        status = True
        else:
            error_message(ReadTemplate.GEN_VERBOSE, 'check template directory')
        return template_list, status

    def __str__(self):
        '''
            Dunder method for ReadTemplate.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, FileChecking.__str__(self)
        )
