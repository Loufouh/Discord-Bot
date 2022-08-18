from test.dummies.queue_player.test_case import TestCase

class TestQueuePlayer_next(TestCase):
    def test(self):
        self.player.next()

        self.assertTrue(self.player._calledNext)

