import unittest
import discord

from dummies.context import Context_dummy
from dummies.voice_protocol import VoiceProtocol_dummy

class TestVoiceProtocol_stop(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()

        self.voiceProtocol = self.ctx.voice_client

        self.source = discord.AudioSource()

    def test_normal(self):
        self.voiceProtocol.play(self.source)
        self.voiceProtocol.stop()

        self.assertFalse(self.voiceProtocol.is_playing())
        self.assertIsNone(self.voiceProtocol.source)
        self.assertTrue(self.voiceProtocol._calledStop)

    def test_twice(self):
        self.voiceProtocol.play(self.source)
        self.voiceProtocol.stop()
        self.voiceProtocol.stop()

        self.assertFalse(self.voiceProtocol.is_playing())
        self.assertIsNone(self.voiceProtocol.source)
        self.assertTrue(self.voiceProtocol._calledStop)

    def test_no_playing(self):
        self.voiceProtocol.stop()

        self.assertFalse(self.voiceProtocol.is_playing())
        self.assertIsNone(self.voiceProtocol.source)
        self.assertTrue(self.voiceProtocol._calledStop)
    
    def test_after(self):
        isAfterExecuted = False 
       
        def after():
            nonlocal isAfterExecuted
            isAfterExecuted = True

        self.voiceProtocol.play(self.source, after=after)
        self.voiceProtocol.stop()

        self.assertTrue(isAfterExecuted)
        self.assertFalse(self.voiceProtocol.is_playing())
        self.assertIsNone(self.voiceProtocol.source)
        self.assertTrue(self.voiceProtocol._calledStop)

