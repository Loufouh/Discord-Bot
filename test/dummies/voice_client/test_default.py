import unittest

from dummies.voice_client import VoiceClient_dummy
from dummies.context import Context_dummy

class TestVoiceClient_default(unittest.IsolatedAsyncioTestCase):
    def test(self):
        ctx = Context_dummy()
        voiceClient = VoiceClient_dummy(ctx)

        self.assertEqual(voiceClient.ctx, ctx)
        self.assertIsNone(voiceClient.source)

        self.assertFalse(voiceClient.is_playing())
        self.assertFalse(voiceClient.is_paused())

        self.assertFalse(voiceClient._calledStop)
        self.assertFalse(voiceClient._calledPause)
        self.assertFalse(voiceClient._calledResume)

