import unittest
import discord

from dummies.voice_protocol import VoiceProtocol_dummy
from dummies.context import Context_dummy

class TestVoiceProtocol__end_playing(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()

        self.voiceProtocol = self.ctx.voice_client

    def test(self):
        self.voiceProtocol.play(discord.AudioSource())
        self.voiceProtocol._end_playing()

        self.assertFalse(self.voiceProtocol.is_playing())
        self.assertIsNone(self.voiceProtocol.source)

