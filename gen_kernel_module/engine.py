# -*- coding: UTF-8 -*-

'''
Module
    engine.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_kernel_module is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_kernel_module is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Engine orchestrating the initialization and execution of gen_kernel_module.
'''

from __future__ import annotations

from collections.abc import Mapping
from logging import INFO, ERROR
from sys import stdout

from ats_utilities.base.engine import Base
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.exceptions import ATSValueError, ATSTypeError

from gen_kernel_module.setup.bundle import GenKernelModuleBundle
from gen_kernel_module.setup.validator import GenKernelModuleBundleValidator
from gen_kernel_module.infrastructure.cli.icli import ICLI

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_kernel_module'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_kernel_module/blob/dev/LICENSE'
__version__ = '1.0.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenKernelModule(Base):
    '''
        Engine orchestrating the initialization and execution of gen_kernel_module.

        It defines:

            :attributes:
                | _is_initialized - The flag indicating whether the gen_kernel_module engine is initialized.
                | _logger - The logger for logging messages during initialization and execution.
                | _cli - The adapter for the command line interface.
            :methods:
                | __init__ - Initializes the gen_kernel_module engine with adapters and services.
                | process - Processes the gen_kernel_module commands.
    '''

    _is_initialized: bool
    _logger: ILogger
    _cli: ICLI

    def __init__(self, bundle: GenKernelModuleBundle) -> None:
        '''
            Initializes the gen_kernel_module engine with adapters and services.

            :param bundle: gen_kernel_module bundle containing adapters and services.
            :exceptions: None.
        '''
        self._is_initialized = False

        try:
            GenKernelModuleBundleValidator.validate(bundle)

            # Initialize base engine
            super().__init__(bundle.base)

            # Mark as not initialized (waiting for other components to be initialized)
            self._is_initialized = False

            # Setting up primary inbound adapter (CLI interface)
            self._cli = bundle.cli

            # Mark as initialized (all components initialized)
            self._is_initialized = all([
                component.is_initialized() for component in [
                    bundle.base.option_manager,
                    bundle.service,
                    bundle.subprocessor,
                    self._cli
                ] if component
            ])

            # Setting up logger for tool engine
            self._logger = self.get_context().logger
            self._logger.write_log(INFO, '✅ gen_kernel_module: engine initialized successfully!')

        except (ATSValueError, ATSTypeError) as exc:
            stdout.write(f'❌ gen_kernel_module: {exc}!\n')

        except Exception as exc:
            stdout.write(f'❌ gen_kernel_module unexpected exception: {exc}!\n')

    def process(self) -> bool:
        '''
            Processes the gen_kernel_module commands.

            :return: True if successful, False otherwise.
            :exceptions: None.
        '''
        result: Mapping[str, object] = {}

        try:
            if self.is_initialized():
                self._logger.write_log(INFO, '🔥 Starting execution command...')
                result = self._cli.run()
                self._logger.write_log(INFO, '✅ Execution finished!')

                if result.get("returncode") != 0:
                    self._logger.write_log(ERROR, f'❌ gen_kernel_module: {result.get("stderr") or "failed!"}')
                    return False
                else:
                    self._logger.write_log(INFO, '✅ gen_kernel_module: done!')
                    self._logger.write_log(INFO, '✅ gen_kernel_module: exiting successfully!')
                    return True
            else:
                self._logger.write_log(ERROR, '❌ gen_kernel_module: engine not initialized!')
                return False

        except (ATSValueError, ATSTypeError) as exc:
            self._logger.write_log(ERROR, f'❌ gen_kernel_module: {exc}!')
            return False

        except Exception as exc:
            self._logger.write_log(ERROR, f'❌ gen_kernel_module unexpected exception: {exc}!')
            return False
