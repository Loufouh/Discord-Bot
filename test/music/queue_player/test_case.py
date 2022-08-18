import unittest
import discord

from dummies.context import Context_dummy
from dummies.voice_client import VoiceClient_dummy

from music.queue import Queue
from music.queue_player import get_queue_player

class TestCase(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        await self.setUp_context()
        self.setUp_voiceClient()
        self.setUp_queue()
        self.setUp_player()
        self.setUp_sources()

    async def setUp_context(self):
        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()

    def setUp_voiceClient(self):
        self.voiceClient = VoiceClient_dummy(self.ctx)

    def setUp_queue(self):
        self.queue = Queue()

    def setUp_player(self):
        self.player = get_queue_player()
        self.player.set_queue(self.queue)

    def setUp_sources(self):
        self.sources = [discord.AudioSource() for _ in range(10)]


    def assert_playing_source(self, source):
        self.assertTrue(self.voiceClient.is_playing())
        self.assertEqual(self.voiceClient.source, source)

    def assert_not_playing(self):
        self.assertFalse(self.voiceClient.is_playing())

    def add_sources(self, *sources):
        for source in sources:
            self.queue.add(source)

