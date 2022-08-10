import unittest
from config import config

from commands.objects.join import JoinCommand, get_command, reset
from dummies.commands.objects.command import Command_dummy

class TestJoinCommand_get_command(unittest.TestCase):
    def tearDown(self):
        config['isTesting'] = True
        reset()

    def test_during_production(self):
        config['isTesting'] = False

        command = get_command()

        self.assertIsInstance(command, JoinCommand)

    def test_call_twice(self):
        config['isTesting'] = False

        command1 = get_command()
        command2 = get_command()

        self.assertEqual(command1, command2)

    def test_during_test(self):
        command = get_command()

        self.assertIsInstance(command, Command_dummy)

