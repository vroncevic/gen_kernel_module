# -*- coding: UTF-8 -*-

"""
 Module
     write_template.py
 Copyright
     Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
     generate_kernel_module is free software: you can redistribute it and/or
     modify it under the terms of the GNU General Public License as published
     by the Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     generate_kernel_module is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define class WriteTemplate with attribute(s) and method(s).
     Write template content with parameters to a file setup.py.
"""

import sys
from inspect import stack
from os import getcwd, chmod
from string import Template

try:
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


class WriteTemplate(object):
    """
        Define class WriteTemplate with attribute(s) and method(s).
        Write template content with parameters to a file setup.py.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __check_setup - Flag for checking setup
            method:
                __init__ - Initial constructor
                get_check_setup - Getter status of checking setup
                write - Write a template content to a file setup.py
    """

    __slots__ = ('VERBOSE', '__check_setup')
    VERBOSE = 'GEN_KERNEL_MODULE::LKM::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        """
            Initial constructor
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(WriteTemplate.VERBOSE, verbose, 'Initial writer')
        self.__check_setup = False

    def get_check_setup(self):
        """
            Getter status of checking setup
            :return: Status of checking setup
            :rtype: <bool>
        """
        return self.__check_setup

    def write(self, setup_content, module_name, verbose=False):
        """
            Write setup content to file.
            :param setup_content: Template content
            :type setup_content: <dict>
            :param module_name: Parameter module name
            :type module_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
            :exception: ATSBadCallError | ATSTypeError
        """
        status, setup = False, None
        func, current_dir = stack()[0][3], getcwd()
        setup_txt = 'First argument: expected setup_content <dict> object'
        setup_msg = "{0} {1} {2}".format('def', func, setup_txt)
        module_txt = 'First argument: expected module_name <str> object'
        module_msg = "{0} {1} {2}".format('def', func, module_txt)
        if setup_content is None or not setup_content:
            raise ATSBadCallError(setup_msg)
        if not isinstance(setup_content, dict):
            raise ATSTypeError(setup_msg)
        if     module_name is None or not module_name:
            raise ATSBadCallError(module_msg)
        if not isinstance(module_name, str):
            raise ATSTypeError(module_msg)
        self.__check_setup = True
        verbose_message(
            WriteTemplate.VERBOSE, verbose, 'Generate module', module_name
        )
        for setup in setup_content.values():
            template_content = Template(setup[1])
            template_path = "{0}/{1}".format(current_dir, setup[0])
            if template_content:
                with open(template_path, 'w') as setup_file:
                    verbose_message(
                        WriteTemplate.VERBOSE, verbose,
                        "Write source module: {0}".format(setup[0])
                    )
                    setup_file.write(
                        template_content.substitute(
                            {'LKM': "{0}".format(module_name)}
                        )
                    )
                    chmod(template_path, 0o666)
                    status = True
        return True if status else False
