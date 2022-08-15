import unittest

from config import config

from music.queue_player import QueuePlayer, get_queue_player

class TestQueuePlayer_get_queue_player(unittest.TestCase):
    def test_normal_play(self):
        player = get_queue_player()

        self.assertIsInstance(player, QueuePlayer)

    def test_normal_play_twice(self):
        player1 = get_queue_player()
        player2 = get_queue_player()

        self.assertEqual(player1, player2)

