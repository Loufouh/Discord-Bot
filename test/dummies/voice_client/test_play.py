import unittest
import discord

from dummies.context import Context_dummy
from dummies.voice_client import VoiceClient_dummy

class TestVoiceClient_play(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()

        self.voiceClient = self.ctx.voice_client

        self.source = discord.AudioSource()

    def test_normal_no_after(self):
        self.voiceClient.play(self.source)

        self.assertTrue(self.voiceClient.is_playing())
        self.assertEqual(self.voiceClient.source, self.source)

    def test_normal_with_after(self):
        isAfterExecuted = False

        def after(error):
            nonlocal isAfterExecuted
            isAfterExecuted = True
        
        self.assertFalse(isAfterExecuted)

        self.voiceClient.play(self.source, after=after)
        self.voiceClient._end_playing()

        self.assertTrue(isAfterExecuted)
    
    def test_source_wrong_type(self):
        with self.assertRaises(TypeError):
            self.voiceClient.play(10)

    def test_after_not_callable(self):
        with self.assertRaises(TypeError):
            self.voiceClient.play(self.source, 3)

    async def test_not_connected(self):
        await self.ctx._disconnect()

        with self.assertRaises(discord.ClientException):
            self.voiceClient.play(self.source)

    def test_already_playing(self):
        self.voiceClient.play(self.source)

        with self.assertRaises(discord.ClientException):
            self.voiceClient.play(self.source)

