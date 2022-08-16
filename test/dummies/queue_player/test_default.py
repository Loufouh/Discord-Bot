import unittest

from dummies.queue_player import QueuePlayer_dummy

class TestQueuePlayer_default(unittest.TestCase):
    def setUp(self):
        self.player = QueuePlayer_dummy()

    def test(self):
        self.assertIsNone(self.player.voiceClient)

        self.assertFalse(self.player._calledNext)
        self.assertFalse(self.player._calledPlay)

