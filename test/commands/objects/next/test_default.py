import unittest

from commands.objects.next import NextCommand
from music.queue_player import QueuePlayer

class TestNextCommand_default(unittest.TestCase):
    def test(self):
        command = NextCommand()

        self.assertIsInstance(command.player, QueuePlayer)

