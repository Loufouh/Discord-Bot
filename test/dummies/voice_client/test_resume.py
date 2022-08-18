import discord

from test.dummies.voice_client.test_case import TestCase

class TestVoiceClient_resume(TestCase):
    def test(self):
        self.voiceClient.play(discord.AudioSource())
        self.voiceClient.resume()

        self.assertTrue(self.voiceClient._calledResume)
        self.assertTrue(self.voiceClient.is_playing())
        self.assertFalse(self.voiceClient.is_paused())

