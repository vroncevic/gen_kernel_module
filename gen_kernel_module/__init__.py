# -*- coding: UTF-8 -*-

'''
 Module
     gen_kernel_module.py
 Copyright
     Copyright (C) 2017 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class GenKernelModule with attribute(s) and method(s).
     Load a base info, create an CLI interface and run operation(s).
'''

import sys
from os import getcwd

try:
    from six import add_metaclass
    from pathlib import Path
    from gen_kernel_module.lkm import GenLKM
    from ats_utilities.logging import ATSLogger
    from ats_utilities.cli.cfg_cli import CfgCLI
    from ats_utilities.cooperative import CooperativeMeta
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.success import success_message
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


@add_metaclass(CooperativeMeta)
class GenKernelModule(CfgCLI):
    '''
        Defined class GenKernelModule with attribute(s) and method(s).
        Load a base info, create an CLI interface and run operation(s).
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | CONFIG - tool info file path.
                | LOG - tool log file path.
                | OPS - list of tool options.
                | logger - logger object API.
            :methods:
                | __init__ - initial constructor.
                | process - process and generate module setup.py.
                | __str__ - dunder method for GenKernelModule.
    '''

    GEN_VERBOSE = 'GEN_KERNEL_MODULE'
    CONFIG = '/conf/gen_kernel_module.cfg'
    LOG = '/log/gen_kernel_module.log'
    OPS = ['-g', '--gen', '-v', '--verbose', '--version']

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option
            :type verbose: <bool>
            :exceptions: None
        '''
        current_dir = Path(__file__).resolve().parent
        base_info = '{0}{1}'.format(current_dir, GenKernelModule.CONFIG)
        CfgCLI.__init__(self, base_info, verbose=verbose)
        verbose_message(GenKernelModule.GEN_VERBOSE, verbose, 'init tool info')
        self.logger = ATSLogger(
            GenKernelModule.GEN_VERBOSE.lower(),
            '{0}{1}'.format(current_dir, GenKernelModule.LOG),
            verbose=verbose
        )
        if self.tool_operational:
            self.add_new_option(
                GenKernelModule.OPS[0], GenKernelModule.OPS[1],
                dest='gen', help='generate Linux Kernel Module'
            )
            self.add_new_option(
                GenKernelModule.OPS[2], GenKernelModule.OPS[3],
                action='store_true', default=False,
                help='activate verbose mode for generation'
            )
            self.add_new_option(
                GenKernelModule.OPS[4], action='version', version=__version__
            )

    def process(self, verbose=False):
        '''
            Process and run operation.

            :param verbose: enable/disable verbose option
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: None
        '''
        status = False
        if self.tool_operational:
            num_of_args_sys = len(sys.argv)
            if num_of_args_sys > 1:
                operation = sys.argv[1]
                if operation not in GenKernelModule.OPS:
                    sys.argv.append('-h')
            else:
                sys.argv.append('-h')
            args, current_dir = self.parse_args(sys.argv[1:]), getcwd()
            setup_path = '{0}/{1}'.format(current_dir, args.gen)
            setup_exists = Path(setup_path).exists()
            if not setup_exists:
                if bool(args.gen):
                    print(
                        '{0} {1} [{2}]'.format(
                            '[{0}]'.format(GenKernelModule.GEN_VERBOSE),
                            'generating kernel module', args.gen
                        )
                    )
                    generator = GenLKM(verbose=verbose)
                    status = generator.gen_module(
                        '{0}'.format(args.gen), verbose=verbose
                    )
                    if status:
                        success_message(GenKernelModule.GEN_VERBOSE, 'done\n')
                        self.logger.write_log(
                            '{0} {1} done'.format(
                                'generating kernel module', args.gen
                            ), ATSLogger.ATS_INFO
                        )
                    else:
                        error_message(
                            GenKernelModule.GEN_VERBOSE, 'generation failed'
                        )
                        self.logger.write_log(
                            'generation failed', ATSLogger.ATS_ERROR
                        )
                else:
                    error_message(
                        GenKernelModule.GEN_VERBOSE, 'provide package name'
                    )
                    self.logger.write_log(
                        'provide package name', ATSLogger.ATS_ERROR
                    )
            else:
                error_message(
                    GenKernelModule.GEN_VERBOSE, 'project already exist'
                )
                self.logger.write_log(
                    'project already exist', ATSLogger.ATS_ERROR
                )
        else:
            error_message(
                GenKernelModule.GEN_VERBOSE, 'tool is not operational'
            )
            self.logger.write_log(
                'tool is not operational', ATSLogger.ATS_ERROR
            )
        return status

    def __str__(self):
        '''
            Dunder method for GenKernelModule.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, CfgCLI.__str__(self), str(self.logger)
        )
