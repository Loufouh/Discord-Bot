import unittest

from test.music.dummies.voice_client import VoiceClient_dummy

from music.queue import Queue
from music.queue_player import get_queue_player

class TestCase(unittest.TestCase):
    def setUp(self):
        self.voiceClient = VoiceClient_dummy()
        self.queue = Queue()

        self.player = get_queue_player()
        self.player.set_queue(self.queue)

    def assert_playing_source(self, source):
        self.assertTrue(self.voiceClient.is_playing())
        self.assertEqual(self.voiceClient.currentSource, source)

    def assert_not_playing(self):
        self.assertFalse(self.voiceClient.is_playing())

    def add_sources(self, *sources):
        for source in sources:
            self.queue.add(source)

