# -*- coding: UTF-8 -*-
# module_selector.py
# Copyright (C) 2018 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# gen_kernel_module is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gen_kernel_module is distributed in the hope that it will be useful, but
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
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.console_io.error import error_message
except ImportError as e:
    msg = "\n{0}\n{1}\n".format(__file__, e)
    sys.exit(msg)  # Force close python ATS ##################################

__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2018, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"


class ModuleSelector(object):
    """
        Define class ModuleSelector with attribute(s) and method(s).
        Selecting kernel module type for generating process.
        It defines:
            attribute:
                __slots__ - Setting class slots
                VERBOSE - Console text indicator for current process-phase
                CharDev - 0 LKM Charachter Device
                BlkDev - 1 LKM Block Device
                NetDev - 2 LKM Network Interface
                VMADev - 3 LKM Virtual Memory Address
                Cancel - 4 Cancel option
                __MODULES - Dictionary with option/description
            method:
                choose_module - Selecting module-type for generating process
    """

    __slots__ = (
        'VERBOSE',
        'CharDev',
        'BlkDev',
        'NetDev',
        'VMADev',
        'Cancel',
        '__MODULES'
    )
    VERBOSE = 'GEN_KERNEL_MODULE::LKM::MODULE_SELECTOR'
    CharDev, BlkDev, NetDev, VMADev, Cancel = range(5)
    __MODULES = {
        CharDev: "LKM Charachter Device",
        BlkDev: "LKM Block Device",
        NetDev: 'LKM Network Interface',
        VMADev: 'LKM Virtual Memory Address',
        Cancel: "Cancel"
    }

    @classmethod
    def choose_module(cls, verbose=False):
        """
            Choose type of kernel module.
            :param verbose: Enable/disable verbose option
            :type verbose: <bool>
            :return: Type of data model {0, 1, 2, 3, 4}
            :rtype: <int>
            :exceptions: None
        """
        verbose_message(cls.VERBOSE, verbose, 'Loading options')
        print("\n {0}".format('module option list:'))
        for key in sorted(cls.__MODULES):
            print("  {0} {1}".format(key, cls.__MODULES[key]))
        while True:
            module_type = int(input(' Select module: '))
            if module_type not in cls.__MODULES.keys():
                error_message(cls.VERBOSE, 'Not an appropriate choice.')
            else:
                break
        verbose_message(cls.VERBOSE, verbose, 'Selected option', module_type)
        return module_type

