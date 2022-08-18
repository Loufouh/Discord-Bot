import discord

from test.dummies.voice_client.test_case import TestCase

class TestVoiceClient__end_playing(TestCase):
    def test(self):
        self.voiceClient.play(discord.AudioSource())
        self.voiceClient._end_playing()

        self.assertFalse(self.voiceClient.is_playing())
        self.assertIsNone(self.voiceClient.source)

