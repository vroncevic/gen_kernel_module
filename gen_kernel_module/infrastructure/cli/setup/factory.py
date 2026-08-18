# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Encapsulates core CLI components for simplification of CLI bundle.
'''

from __future__ import annotations

from ats_utilities.option.imanager import IOptionManager

from gen_kernel_module.core.service.iservice import IService
from gen_kernel_module.infrastructure.cli.setup.options import CLIBundleOptions
from gen_kernel_module.infrastructure.cli.setup.opt_validator import CLIBundleOptionsValidator
from gen_kernel_module.infrastructure.cli.setup.bundle import CLIBundle
from gen_kernel_module.infrastructure.cli.setup.keys import CLIBundleKeys
from gen_kernel_module.infrastructure.cli.setup.registry import CLIBundleRegistry
from gen_kernel_module.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from gen_kernel_module.infrastructure.command.command import CommandBundle
from gen_kernel_module.infrastructure.command.icommand_definition import ICommandDefinition
from gen_kernel_module.infrastructure.command.icommand_executor import ICommandExecutor
from gen_kernel_module.infrastructure.command.gen_kernel_module_command_definition import GenKernelModuleCommandDefinition
from gen_kernel_module.infrastructure.command.gen_kernel_module_command_executor import GenKernelModuleCommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_kernel_module'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_kernel_module/blob/dev/LICENSE'
__version__ = '1.4.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CLIBundleFactory:
    '''
        Factory for creating the CLI bundle.

        It defines:

            :methods:
                | create_bundle - Creates the CLI bundle with optional pre-configured options.
                | get_version - Returns the factory version.
    '''

    @classmethod
    def create_bundle(cls, options: CLIBundleOptions) -> CLIBundle:
        '''
            Creates the CLI bundle with optional pre-configured options.

            :param options: The CLI bundle options.
            :return: The CLI bundle.
            :exceptions:
                | ATSValueError: The CLI bundle options must be provided and have proper values.
                | ATSTypeError:  The CLI bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The CLI bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The CLI bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The CLI bundle must be provided and have proper values.
                | ATSTypeError:  The CLI bundle must be an instance of CLIBundle and
                |                its attributes must be instances of their respective types.
        '''
        CLIBundleOptionsValidator.validate(options)

        service: IService | None = options.get(CLIBundleKeys.OPTION_SERVICE) if options else None
        parser: IOptionManager | None = options.get(CLIBundleKeys.OPTION_PARSER) if options else None

        service_definition: ICommandDefinition = GenKernelModuleCommandDefinition()
        service_executor: ICommandExecutor = GenKernelModuleCommandExecutor(definition=service_definition)
        service_cmd: CommandBundle = CommandBundle(definition=service_definition, executor=service_executor)

        return CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(service=service, parser=parser, commands=[service_cmd])
        )

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the factory version.

            :return: The factory version.
            :exceptions: None.
        '''
        return __version__
