# -*- coding: UTF-8 -*-

'''
Module
    opt_validator_test.py
Info
    Unit tests for GenKernelModuleBundleOptionsValidator class.
'''

from __future__ import annotations

import unittest

from gen_kernel_module.setup.opt_validator import GenKernelModuleBundleOptionsValidator


class TestGenKernelModuleBundleOptionsValidator(unittest.TestCase):

    def test_validate_success(self) -> None:
        options = {'info_file': 'some_path'}
        GenKernelModuleBundleOptionsValidator.validate(options)

    def test_validate_none(self) -> None:
        with self.assertRaises(Exception):
            GenKernelModuleBundleOptionsValidator.validate(None)

    def test_validate_invalid_type(self) -> None:
        with self.assertRaises(Exception):
            GenKernelModuleBundleOptionsValidator.validate("not_a_mapping")

    def test_validate_invalid_option_type(self) -> None:
        with self.assertRaises(Exception):
            options = {'info_file': 123}
            GenKernelModuleBundleOptionsValidator.validate(options)

    def test_is_valid_success(self) -> None:
        options = {'info_file': 'some_path'}
        self.assertTrue(GenKernelModuleBundleOptionsValidator.is_valid(options))

    def test_is_valid_failure(self) -> None:
        self.assertFalse(GenKernelModuleBundleOptionsValidator.is_valid(None))
        self.assertFalse(GenKernelModuleBundleOptionsValidator.is_valid("not_a_mapping"))
        self.assertFalse(GenKernelModuleBundleOptionsValidator.is_valid({'info_file': 123}))
