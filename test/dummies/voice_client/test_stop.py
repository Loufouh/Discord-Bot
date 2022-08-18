import discord

from test.dummies.voice_client.test_case import TestCase


class TestVoiceClient_stop(TestCase):
    async def asyncSetUp(self):
        await super().asyncSetUp()

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
       
        def after(error):
            nonlocal isAfterExecuted
            isAfterExecuted = True

        self.voiceClient.play(self.source, after=after)
        self.voiceClient.stop()

        self.assertTrue(isAfterExecuted)
        self.assertFalse(self.voiceClient.is_playing())
        self.assertIsNone(self.voiceClient.source)
        self.assertTrue(self.voiceClient._calledStop)

