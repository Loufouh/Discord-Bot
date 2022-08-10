import unittest

from config import config

from commands.objects.command import get_command, reset
from commands.objects.play import PlayCommand
from commands.objects.join import JoinCommand

from dummies.commands.objects.command import Command_dummy

class TestCommand_get_command(unittest.TestCase):
    def setUp(self):
        reset()

    def tearDown(self):
        config['isTesting'] = True

    def test_normal_play(self):
        config['isTesting'] = False

        command = get_command(PlayCommand)

        self.assertIsInstance(command, PlayCommand)

    def test_normal_join(self):
        config['isTesting'] = False

        command = get_command(JoinCommand)

        self.assertIsInstance(command, JoinCommand)

    def test_normal_play_twice(self):
        config['isTesting'] = False

        command1 = get_command(PlayCommand)
        command2 = get_command(PlayCommand)

        self.assertEqual(command1, command2)

    def test_normal_play_and_join(self):
        config['isTesting'] = False

        playCommand = get_command(PlayCommand)
        joinCommand = get_command(JoinCommand)

        self.assertIsInstance(playCommand, PlayCommand)
        self.assertIsInstance(joinCommand, JoinCommand)

    def test_testing_play(self):
        command = get_command(PlayCommand)

        self.assertIsInstance(command, Command_dummy)

