# -*- coding: UTF-8 -*-
# gen_lkm.py
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

try:

    from lkm.module_selector import ModuleSelector

    from lkm.read_template import ReadTemplate
    from lkm.write_template import WriteTemplate

    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.error import error_message
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


class GenLKM(object):
    """
        Define class GenLKM with attribute(s) and method(s).
        Generate kernel module file by template and parameters.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                __reader - Reader API
                __writer - Writer API
            method:
                __init__ - Initial constructor
                gen_module - Generate kernel module.
    """

    __slots__ = ('VERBOSE', '__reader', '__writer')
    VERBOSE = 'GEN_KERNEL_MODULE::LKM::GEN_LKM'

    def __init__(self, verbose=False):
        """
            Initial constructor
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        """
        verbose_message(GenLKM.VERBOSE, verbose, 'Initial generator')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)

    def gen_module(self, module_name, verbose=False):
        """
            Generate kernel module.
            :param module_name: Parameter package name
            :type module_name: <str>
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
            :exceptions: ATSBadCallError | ATSTypeError
        """
        func, status, module_content = stack()[0][3], False, None
        module_name_txt = 'Argument: expected module_name <str> object'
        module_msg = "{0} {1} {2}".format('def', func, module_name_txt)
        if module_name is None or not module_name:
            raise ATSBadCallError(module_msg)
        if not isinstance(module_name, str):
            raise ATSTypeError(module_msg)
        verbose_message(
            GenLKM.VERBOSE, verbose, 'Generating kernel module', module_name
        )
        module_type = ModuleSelector.choose_module(verbose=verbose)
        if module_type != ModuleSelector.Cancel:
            module_content = self.__reader.read(module_type, verbose=verbose)
            if module_content:
                status = self.__writer.write(
                    module_content, module_name, verbose=verbose
                )
        return True if status else False

