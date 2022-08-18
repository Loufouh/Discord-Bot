from test.dummies.queue_player.test_case import TestCase

class TestQueuePlayer_default(TestCase):
    def test(self):
        self.assertIsNone(self.player.queue)
        self.assertIsNone(self.player.voiceClient)

        self.assertFalse(self.player._calledNext)
        self.assertFalse(self.player._calledPlay)

