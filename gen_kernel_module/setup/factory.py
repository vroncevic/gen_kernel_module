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
    Factory for creating the gen_kernel_module bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextBundleFactory

from gen_kernel_module.setup.bundle import GenKernelModuleBundle
from gen_kernel_module.setup.options import GenKernelModuleBundleOptions
from gen_kernel_module.setup.registry import GenKernelModuleBundleRegistry
from gen_kernel_module.setup.dependencies import GenKernelModuleBundleDependencies
from gen_kernel_module.setup.opt_validator import GenKernelModuleBundleOptionsValidator
from gen_kernel_module.setup.keys import GenKernelModuleBundleKeys
from gen_kernel_module.core.service.engine import Service
from gen_kernel_module.infrastructure.subprocessor import SubProcessor
from gen_kernel_module.infrastructure.cli.engine import CLI
from gen_kernel_module.infrastructure.cli.setup.bundle import CLIBundle
from gen_kernel_module.infrastructure.cli.setup.dependencies import CLIBundleDependencies
from gen_kernel_module.infrastructure.cli.setup.registry import CLIBundleRegistry
from gen_kernel_module.infrastructure.command.command import CommandBundle
from gen_kernel_module.infrastructure.command.gen_kernel_module_command_definition import GenKernelModuleCommandDefinition
from gen_kernel_module.infrastructure.command.gen_kernel_module_command_executor import GenKernelModuleCommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_kernel_module'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_kernel_module/blob/dev/LICENSE'
__version__ = '1.0.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenKernelModuleBundleFactory:
    '''
        Factory for creating the gen_kernel_module bundle.

        It defines:

            :attributes:
                | _info_file - Path to the gen_kernel_module info file.
            :methods:
                | create_bundle - Creates the gen_kernel_module bundle with optional pre-configured options.
    '''

    _info_file: str = 'gen_kernel_module/infrastructure/config/gen_kernel_module.cfg'

    @classmethod
    def create_bundle(cls, options: GenKernelModuleBundleOptions | None = None) -> GenKernelModuleBundle:
        '''
            Creates the gen_kernel_module bundle with optional pre-configured options.

            :param options: The pre-configured options for the gen_kernel_module bundle.
            :return: The gen_kernel_module bundle.
            :exceptions:
                | ATSValueError: The gen_kernel_module bundle options must be provided and have proper values.
                | ATSTypeError:  The gen_kernel_module bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_kernel_module bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_kernel_module bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_kernel_module bundle must be provided and have proper values.
                | ATSTypeError:  The gen_kernel_module bundle must be an instance of GenKernelModuleBundle and
                |                its attributes must be instances of their respective types.
        '''
        if options is not None:
            GenKernelModuleBundleOptionsValidator.validate(options)

        info_file = options.get(GenKernelModuleBundleKeys.OPTION_INFO_FILE) if options else cls._info_file

        context_bundle: ContextBundle = ContextBundleFactory.create_bundle()

        base_bundle: BaseBundle = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file=info_file,
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        subprocessor: SubProcessor = SubProcessor(generator=base_bundle.generation_manager)

        service: Service = Service(subprocessor=subprocessor)

        gen_kernel_module_definition: GenKernelModuleCommandDefinition = GenKernelModuleCommandDefinition()

        gen_kernel_module_bundle: CommandBundle = CommandBundle(
            definition=gen_kernel_module_definition,
            executor=GenKernelModuleCommandExecutor(gen_kernel_module_definition)
        )

        cli_bundle: CLIBundle = CLIBundleRegistry.create_bundle(
            dependencies=CLIBundleDependencies(
                service=service,
                parser=base_bundle.option_manager,
                commands=[gen_kernel_module_bundle]
            )
        )

        cli: CLI = CLI(cli_bundle)

        return GenKernelModuleBundleRegistry.create_bundle(
            dependencies=GenKernelModuleBundleDependencies(
                base=base_bundle,
                service=service,
                subprocessor=subprocessor,
                cli=cli
            )
        )
