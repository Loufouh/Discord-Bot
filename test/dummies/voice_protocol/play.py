import unittest
import discord

from dummies.context import Context_dummy
from dummies.voice_protocol import VoiceProtocol_dummy

class TestVoiceProtocol_play(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()

        self.voiceProtocol = self.ctx.voice_client

        self.source = discord.AudioSource()

    def test_normal_no_after(self):
        self.voiceProtocol.play(self.source)

        self.assertTrue(self.voiceProtocol.is_playing())
        self.assertEqual(self.voiceProtocol.source, self.source)

    def test_normal_with_after(self):
        isAfterExecuted = False

        def after():
            nonlocal isAfterExecuted
            isAfterExecuted = True
        
        self.assertFalse(isAfterExecuted)

        self.voiceProtocol.play(self.source, after=after)
        self.voiceProtocol._end_playing()

        self.assertTrue(isAfterExecuted)
    
    def test_source_wrong_type(self):
        with self.assertRaises(TypeError):
            self.voiceProtocol.play(10)

    def test_after_not_callable(self):
        with self.assertRaises(TypeError):
            self.voiceProtocol.play(self.source, 3)

    async def test_not_connected(self):
        await self.ctx._disconnect()

        with self.assertRaises(discord.ClientException):
            self.voiceProtocol.play(self.source)

    def test_already_playing(self):
        self.voiceProtocol.play(self.source)

        with self.assertRaises(discord.ClientException):
            self.voiceProtocol.play(self.source)

