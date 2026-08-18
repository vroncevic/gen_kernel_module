# -*- coding: UTF-8 -*-

'''
Module
    engine_test.py
Info
    Unit tests for CLI class.
'''

from __future__ import annotations

import unittest
from unittest.mock import Mock

from ats_utilities.exceptions import ATSValueError
from ats_utilities.option.imanager import IOptionManager

from gen_kernel_module.infrastructure.cli.engine import CLI
from gen_kernel_module.infrastructure.cli.setup.bundle import CLIBundle
from gen_kernel_module.infrastructure.command.command import CommandBundle
from gen_kernel_module.infrastructure.cli.icli import ICLI
from gen_kernel_module.infrastructure.command.icommand_executor import ICommandExecutor


class DummyService:

    def execute(self, *, params: object) -> object:
        return None

    def is_initialized(self) -> bool:
        return True


class DummyCommandDefinition:
    name = "gen"


class DummyCommandExecutor:
    def execute(self, *, params: object, service: object) -> dict[str, object]:
        return {'returncode': 0, 'stdout': 'success', 'stderr': ''}


def create_mock_parser() -> Mock:
    mock_parser = Mock(spec=IOptionManager)
    mock_parser.parse_command.return_value = ("gen", {})

    return mock_parser


class TestCLI(unittest.TestCase):

    def test_cli_init_and_run_success(self) -> None:
        dummy_service = DummyService()
        mock_parser = create_mock_parser()
        dummy_def = DummyCommandDefinition()
        dummy_exec = DummyCommandExecutor()
        
        cmd_bundle = CommandBundle(definition=dummy_def, executor=dummy_exec)
        bundle = CLIBundle(
            service=dummy_service,
            parser=mock_parser,
            commands=[cmd_bundle]
        )

        cli = CLI(bundle)
        self.assertTrue(cli.is_initialized())
        self.assertEqual(cli._executors["gen"], dummy_exec)
        
        result = cli.run()
        self.assertEqual(result['returncode'], 0)

    def test_cli_run_command_not_found(self) -> None:
        dummy_service = DummyService()
        mock_parser = create_mock_parser()
        mock_parser.parse_command.return_value = ("unknown", {})
        
        bundle = CLIBundle(
            service=dummy_service,
            parser=mock_parser,
            commands=[]
        )

        cli = CLI(bundle)
        result = cli.run()
        self.assertEqual(result['returncode'], 1)
        self.assertIn('command not found', result['stderr'])

    def test_cli_run_exception(self) -> None:
        dummy_service = DummyService()
        mock_parser = create_mock_parser()
        mock_parser.parse_command.side_effect = ATSValueError('Unexpected runtime error')
        
        bundle = CLIBundle(
            service=dummy_service,
            parser=mock_parser,
            commands=[]
        )

        cli = CLI(bundle)
        result = cli.run()
        self.assertEqual(result['returncode'], 1)
        self.assertIn('cli::run - Unexpected runtime error', result['stderr'])

    def test_cli_str_representation(self) -> None:
        dummy_service = DummyService()
        mock_parser = create_mock_parser()
        bundle = CLIBundle(
            service=dummy_service,
            parser=mock_parser,
            commands=[]
        )
        cli = CLI(bundle)
        self.assertTrue(isinstance(str(cli), str))

    def test_extra_coverage_for_protocols_and_bundles(self) -> None:
        ICLI.run(None)
        ICLI.is_initialized(None)
        ICommandExecutor.execute(None, params={}, service=None)

        dummy_service = DummyService()
        mock_parser = create_mock_parser()
        bundle = CLIBundle(
            service=dummy_service,
            parser=mock_parser,
            commands=[]
        )
        self.assertIsInstance(bundle.to_dict(), dict)
