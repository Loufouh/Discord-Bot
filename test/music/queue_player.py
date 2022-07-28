import unittest

from test.music.dummy_voice_client import DummyVoiceClient
from music.queue import Queue
from music.queue_player import get_queue_player

class TestQueuePlayer(unittest.TestCase):
    queue = None
    voiceClient = None
    player = None

    def setUp(self):
        self.voiceClient = DummyVoiceClient()
        self.queue = Queue()

        self.player = get_queue_player()
        self.player.set_queue(self.queue)

    def testEmptyQueue(self):
        self.player.play(self.voiceClient)

        self.assertFalse(self.voiceClient.is_playing())

    def testQueueWithOneSource(self):
        self.queue.add('source')

        self.player.play(self.voiceClient)

        self.assertTrue(self.voiceClient.is_playing())
        self.assertEqual(self.voiceClient.currentSource, 'source')

        self.voiceClient.end_playing()

        self.assertFalse(self.voiceClient.is_playing())

    def testQueueWithTwoSources(self):
        self.queue.add('source1')
        self.queue.add('source2')
    
        self.player.play(self.voiceClient)

        self.assertTrue(self.voiceClient.is_playing())
        self.assertEqual(self.voiceClient.currentSource, 'source1')

        self.voiceClient.end_playing()

        self.assertTrue(self.voiceClient.is_playing())
        self.assertEqual(self.voiceClient.currentSource, 'source2')

        self.voiceClient.end_playing()

        self.assertFalse(self.voiceClient.is_playing())

