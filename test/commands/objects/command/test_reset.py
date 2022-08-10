import unittest

from commands.objects.command import reset, get_command, _commands
from commands.objects.play import PlayCommand

class TestCommand_reset(unittest.TestCase):
    def test(self):
        get_command(PlayCommand)
        reset()

        self.assertEqual(len(_commands.keys()), 0)

