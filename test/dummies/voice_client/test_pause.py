import unittest
import discord

from dummies.voice_client import VoiceClient_dummy
from dummies.context import Context_dummy

class TestVoiceClient_pause(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()

        self.voiceClient = self.ctx.voice_client
        
    def test(self):
        self.voiceClient.play(discord.AudioSource())
        self.voiceClient.pause()

        self.assertTrue(self.voiceClient._calledPause)
        self.assertTrue(self.voiceClient.is_playing())
        self.assertTrue(self.voiceClient.is_paused())

