import unittest

from dummies.queue_player import QueuePlayer_dummy

class TestQueuePlayer_default(unittest.TestCase):
    def setUp(self):
        self.player = QueuePlayer_dummy()

    def test(self):
        self.assertFalse(self.player._calledNext)

