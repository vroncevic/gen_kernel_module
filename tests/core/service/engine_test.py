# -*- coding: UTF-8 -*-

'''
Module
    engine_test.py
Info
    Unit tests for Service class.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from gen_kernel_module.core.model.project_setup import ProjectSetup
from gen_kernel_module.core.service.engine import Service
from gen_kernel_module.core.service.isubprocessor import ISubProcessor


class DummySubProcessor:
    def run(self, *, params: object) -> dict[str, object]:
        return {}

    def is_initialized(self) -> bool:
        return True


class TestService(unittest.TestCase):
    def test_service_initialization_success(self) -> None:
        subprocessor = DummySubProcessor()
        service = Service(subprocessor)
        self.assertEqual(service._subprocessor, subprocessor)

    def test_service_initialization_value_error(self) -> None:
        with self.assertRaises(ValueError):
            Service(None)

    def test_service_initialization_type_error(self) -> None:
        with self.assertRaises(TypeError):
            Service("invalid_subprocessor")

    def test_service_execute(self) -> None:
        subprocessor = DummySubProcessor()
        expected_result = {'returncode': 0, 'stdout': 'success', 'stderr': ''}
        subprocessor.run = Mock(return_value=expected_result)
        
        service = Service(subprocessor)
        params = ProjectSetup(chip_config={})
        result = service.execute(params=params)
        
        self.assertEqual(result, expected_result)
        subprocessor.run.assert_called_once_with(params=params)

    def test_service_is_initialized(self) -> None:
        subprocessor = DummySubProcessor()
        subprocessor.is_initialized = Mock(return_value=True)
        
        service = Service(subprocessor)
        self.assertTrue(service.is_initialized())
        subprocessor.is_initialized.assert_called_once()
