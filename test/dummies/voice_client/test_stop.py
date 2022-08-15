import unittest
import discord

from dummies.context import Context_dummy
from dummies.voice_client import VoiceClient_dummy

class TestVoiceClient_stop(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()

        self.voiceClient = self.ctx.voice_client

        self.source = discord.AudioSource()

    def test_normal(self):
        self.voiceClient.play(self.source)
        self.voiceClient.stop()

        self.assertFalse(self.voiceClient.is_playing())
        self.assertIsNone(self.voiceClient.source)
        self.assertTrue(self.voiceClient._calledStop)

    def test_twice(self):
        self.voiceClient.play(self.source)
        self.voiceClient.stop()
        self.voiceClient.stop()

        self.assertFalse(self.voiceClient.is_playing())
        self.assertIsNone(self.voiceClient.source)
        self.assertTrue(self.voiceClient._calledStop)

    def test_no_playing(self):
        self.voiceClient.stop()

        self.assertFalse(self.voiceClient.is_playing())
        self.assertIsNone(self.voiceClient.source)
        self.assertTrue(self.voiceClient._calledStop)
    
    def test_after(self):
        isAfterExecuted = False 
       
        def after():
            nonlocal isAfterExecuted
            isAfterExecuted = True

        self.voiceClient.play(self.source, after=after)
        self.voiceClient.stop()

        self.assertTrue(isAfterExecuted)
        self.assertFalse(self.voiceClient.is_playing())
        self.assertIsNone(self.voiceClient.source)
        self.assertTrue(self.voiceClient._calledStop)

