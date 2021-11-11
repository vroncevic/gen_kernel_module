# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
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
     Defined class GenLKM with attribute(s) and method(s).
     Generate kernel module by template and parameters.
'''

import sys

try:
    from pathlib import Path
    from gen_kernel_module.lkm.config import ProConfig
    from gen_kernel_module.lkm.config.pro_name import ProName
    from gen_kernel_module.lkm.read_template import ReadTemplate
    from gen_kernel_module.lkm.write_template import WriteTemplate
    from ats_utilities.checker import ATSChecker
    from ats_utilities.console_io.error import error_message
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
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


class GenLKM(FileChecking, ProConfig, ProName):
    '''
        Defined class GenLKM with attribute(s) and method(s).
        Generate kernel module by template and parameters.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | PRO_STRUCTURE - template/project structure.
                | CANCEL - cancel id.
                | MODULES - modules key.
                | __reader - reader API.
                | __writer - writer API.
            :methods:
                | __init__ - initial constructor.
                | get_reader - getter for template reader.
                | get_writer - getter for template writer.
                | gen_module - generate kernel module.
                | __str__ - dunder method for GenLKM.
    '''

    GEN_VERBOSE = 'GEN_KERNEL_MODULE::LKM::GEN_LKM'
    PRO_STRUCTURE = '/../conf/project.yaml'
    CANCEL, MODULES = 4, 'modules'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        ProConfig.__init__(self, verbose=verbose)
        ProName.__init__(self, verbose=verbose)
        verbose_message(GenLKM.GEN_VERBOSE, verbose, 'init generator')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)
        project_structure = '{0}{1}'.format(
            Path(__file__).parent, GenLKM.PRO_STRUCTURE
        )
        self.check_path(project_structure, verbose=verbose)
        self.check_mode('r', verbose=verbose)
        self.check_format(project_structure, 'yaml', verbose=verbose)
        if self.is_file_ok():
            yml2obj = Yaml2Object(project_structure)
            self.config = yml2obj.read_configuration()

    def get_reader(self):
        '''
            Getter for template reader.

            :return: template reader object.
            :rtype: <ReadTemplate>
            :exceptions: None
        '''
        return self.__reader

    def get_writer(self):
        '''
            Getter for template writer.

            :return: template writer object.
            :rtype: <WriteTemplate>
            :exceptions: None
        '''
        return self.__writer

    def gen_module(self, module_name, verbose=False):
        '''
            Generate kernel module.

            :param module_name: parameter package name.
            :type module_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: True (success) | False
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:module_name', module_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        self.pro_name, status = module_name, False
        module_type, module_id = self.choose_module(verbose=verbose)
        if module_id != GenLKM.CANCEL:
            templates, status = self.__reader.read(
                module_type, module_name, verbose=verbose
            )
            if all([bool(templates), status]):
                status = self.__writer.write(
                    templates, module_name, verbose=verbose
                )
        else:
            status = True
        return status

    def choose_module(self, verbose=False):
        '''
            Choose type of kernel module.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: data model, type id {0, 1, 2, 3, 4}.
            :rtype: <dict>, <int>
            :exceptions: None
        '''
        type_selected, pro_type_id = None, None
        types = self.config[GenLKM.MODULES]
        pro_types_len = len(types)
        for index, lkm_pro in enumerate(types):
            lkm_pro_key, lkm_option = lkm_pro.keys()[0], 'Cancel'
            if lkm_pro_key != 'cancel':
                lkm_option = lkm_pro[lkm_pro_key][0]['info']
            print('  {0} {1}'.format(index + 1, lkm_option))
        while True:
            try:
                try:
                    input_type = raw_input(' select project type: ')
                except NameError:
                    input_type = input(' select project type: ')
                options = xrange(1, pro_types_len + 1, 1)
            except NameError:
                options = range(1, pro_types_len + 1, 1)
            try:
                if int(input_type) in list(options):
                    type_selected = types[int(input_type) - 1]
                    pro_type_id = int(input_type) - 1
                    break
                raise ValueError
            except ValueError:
                error_message(
                    GenLKM.GEN_VERBOSE, 'not an appropriate choice'
                )
        verbose_message(
            GenLKM.GEN_VERBOSE, verbose, 'selected', type_selected
        )
        return type_selected, pro_type_id

    def __str__(self):
        '''
            Dunder method for GenLKM.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3}, {4}, {5})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            ProConfig.__str__(self), ProName.__str__(self),
            str(self.__reader), str(self.__writer)
        )
