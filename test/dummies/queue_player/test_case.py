import unittest

from dummies.queue_player import QueuePlayer_dummy

class TestCase(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.player = QueuePlayer_dummy()

