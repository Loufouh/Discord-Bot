import unittest

from music.queue_player import QueuePlayer
from commands.objects.start_queue import StartQueueCommand

class TestStartQueueCommand_default(unittest.TestCase):
    def setUp(self):
        self.command = StartQueueCommand()

    def test(self):
        self.assertIsInstance(self.command.player, QueuePlayer)

