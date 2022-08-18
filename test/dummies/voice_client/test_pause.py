import discord

from test.dummies.voice_client.test_case import TestCase


class TestVoiceClient_pause(TestCase):
    def test(self):
        self.voiceClient.play(discord.AudioSource())
        self.voiceClient.pause()

        self.assertTrue(self.voiceClient._calledPause)
        self.assertTrue(self.voiceClient.is_playing())
        self.assertTrue(self.voiceClient.is_paused())

