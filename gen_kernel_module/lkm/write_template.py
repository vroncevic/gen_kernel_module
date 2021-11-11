# -*- coding: UTF-8 -*-

'''
 Module
     write_template.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class WriteTemplate with attribute(s) and method(s).
     Defined API for Writing template content with parameters to files.
'''

import sys
from os import getcwd, chmod, mkdir
from string import Template

try:
    from ats_utilities.checker import ATSChecker
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


class WriteTemplate(FileChecking):
    '''
        Defined class WriteTemplate with attribute(s) and method(s).
        Defined API for Writing template content with parameters to files.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
            :methods:
                | __init__ - initial constructor.
                | write - write a template content to a file setup.py.
                | __str__ - dunder method for WriteTemplate.
    '''

    GEN_VERBOSE = 'GEN_KERNEL_MODULE::LKM::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(WriteTemplate.GEN_VERBOSE, verbose, 'init writer')

    def write(self, template_content, module_name, verbose=False):
        '''
            Write setup content to file.

            :param template_content: parameter template content.
            :type template_content: <list>
            :param module_name: parameter module name.
            :type module_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exception: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('list:template_content', template_content),
            ('str:module_name', module_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        status, statuses = False, []
        module_pro_dir = '{0}/{1}/'.format(getcwd(), module_name)
        mkdir(module_pro_dir)
        for template_setup in template_content:
            lkm_type = template_setup.keys()[0]
            template_factory = Template(template_setup[lkm_type][1])
            module_path = '{0}/{1}'.format(
                getcwd(), template_setup[lkm_type][0]
            )
            if bool(template_factory):
                with open(module_path, 'w') as module_file:
                    verbose_message(
                        WriteTemplate.GEN_VERBOSE, verbose,
                        'write module: {0}'.format(module_path)
                    )
                    module_file.write(
                        template_factory.substitute({
                            'LKM': '{0}'.format(module_name)
                        })
                    )
                    chmod(module_path, 0o666)
                    self.check_path(module_path, verbose=verbose)
                    self.check_mode('w', verbose=verbose)
                    if 'makefile'.capitalize() in module_path:
                        self.check_format(
                            module_path, 'makefile', verbose=verbose
                        )
                    else:
                        self.check_format(
                            module_path, module_path.split('.')[1],
                            verbose=verbose
                        )
                    if self.is_file_ok():
                        statuses.append(True)
                    else:
                        statuses.append(False)
        if all(statuses):
            status = True
        return status

    def __str__(self):
        '''
            Dunder method for WriteTemplate.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1})'.format(
            self.__class__.__name__, FileChecking.__str__(self)
        )
