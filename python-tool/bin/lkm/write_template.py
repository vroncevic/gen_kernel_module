# -*- coding: UTF-8 -*-
# write_template.py
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
from os import getcwd, chmod
from string import Template

try:
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config.config_context_manager import ConfigFile
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


class WriteTemplate(object):
    """
        Define class WriteTemplate with attribute(s) and method(s).
        Write template content with parameters to a file setup.py.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __SETUP_FILE - File name for setup file
                __FORMAT - File format (file extension)
            method:
                __init__ - Initial constructor
                write - Write a template content to a file setup.py
    """

    __slots__ = ('VERBOSE', '__SETUP_FILE', '__FORMAT')
    VERBOSE = 'GEN_KERNEL_MODULE::LKM::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        """
            Initial constructor
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(WriteTemplate.VERBOSE, verbose, 'Initial writer')

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
        status, template = False, None
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
        module = {'LKM': "{0}".format(module_name)}
        for template_key, content_template in setup_content.items():
            template = Template(content_template)
            if "Makefile" in template_key:
                template_key = "Makefile"
            elif "test" in template_key:
                template_key = "test_{0}.c".format(module_name)
            else:
                template_key = "{0}.c".format(module_name)
            verbose_message(WriteTemplate.VERBOSE, verbose, template_key)
            if template:
                with open(template_key, 'w') as setup_file:
                    print("    Write source module: {0}".format(template_key))
                    setup_file.write(template.substitute(module))
                    chmod(template_key, 0o666)
                    status = True
        return True if status else False

