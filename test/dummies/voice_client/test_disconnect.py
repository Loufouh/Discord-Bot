import unittest

from test.dummies.voice_client.test_case import TestCase

class TestVoiceProtocol_disconnect(TestCase):
    async def test(self):
        await self.voiceClient.disconnect()

        self.assertIsNone(self.ctx.voice_client)
        self.assertIsNotNone(self.ctx.author.voice)
        
        self.assertTrue(self.ctx.author.voice.channel._isConnected)

