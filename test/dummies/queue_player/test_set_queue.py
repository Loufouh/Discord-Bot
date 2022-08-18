from test.dummies.queue_player.test_case import TestCase
from music.queue import Queue

class TestQueuePlayer_set_queue(TestCase):
    def setUp(self):
        super().setUp()

        self.queue = Queue()

    def test(self):
        self.player.set_queue(self.queue)

        self.assertEqual(self.player.queue, self.queue)

