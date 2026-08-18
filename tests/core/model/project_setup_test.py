# -*- coding: UTF-8 -*-

'''
Module
    project_setup_test.py
Info
    Unit tests for ProjectSetup class.
'''

from __future__ import annotations

import unittest

from gen_kernel_module.core.model.project_setup import ProjectSetup


class TestProjectSetup(unittest.TestCase):
    def test_project_setup_initialization(self) -> None:
        chip_config = {'key': 'value'}
        setup = ProjectSetup(chip_config=chip_config)
        self.assertEqual(setup.chip_config, chip_config)
