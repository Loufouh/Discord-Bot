import unittest

from dummies.queue_player import QueuePlayer_dummy
from music.queue import Queue

class TestQueuePlayer_set_queue(unittest.TestCase):
    def setUp(self):
        self.player = QueuePlayer_dummy()
        self.queue = Queue()

    def test(self):
        self.player.set_queue(self.queue)

        self.assertEqual(self.player.queue, self.queue)

