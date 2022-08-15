import unittest

from dummies.queue_player import QueuePlayer_dummy

class TestQueuePlayer_next(unittest.TestCase):
    def setUp(self):
        self.player = QueuePlayer_dummy()

    def test(self):
        self.player.next()

        self.assertTrue(self.player._calledNext)

