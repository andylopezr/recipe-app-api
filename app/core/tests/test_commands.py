"""
Tests custom Django management commands.
"""
from unittest.mock import patch

from psycopg2 import OperationError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Tests commands."""

    def test_wait_for_db_ready(self, patched_check):
        """Tests waiting for db if db is ready."""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(database=['default'])