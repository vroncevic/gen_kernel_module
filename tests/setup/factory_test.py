# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenKernelModuleBundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_kernel_module.setup.bundle import GenKernelModuleBundle
from gen_kernel_module.setup.factory import GenKernelModuleBundleFactory


class TestGenKernelModuleBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenKernelModuleBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenKernelModuleBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_kernel_module/infrastructure/config/gen_kernel_module.cfg'}
        bundle = GenKernelModuleBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenKernelModuleBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenKernelModuleBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenKernelModuleBundleFactory.get_version(), '1.4.0')
