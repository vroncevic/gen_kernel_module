# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenKernelModuleBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_kernel_module.setup.keys import GenKernelModuleBundleKeys


class TestGenKernelModuleBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenKernelModuleBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenKernelModuleBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenKernelModuleBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenKernelModuleBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenKernelModuleBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenKernelModuleBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenKernelModuleBundleKeys.OPTION_INFO_FILE, opts)
