import unittest

from dummies.voice_client import VoiceClient_dummy
from dummies.context import Context_dummy

class TestVoiceClient_default(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.ctx = Context_dummy()
        self.voiceClient = VoiceClient_dummy(self.ctx)

    def test(self):
        self.assertEqual(self.voiceClient.ctx, self.ctx)
        self.assertIsNone(self.voiceClient.source)

        self.assertFalse(self.voiceClient.is_playing())
        self.assertFalse(self.voiceClient.is_paused())

        self.assertFalse(self.voiceClient._calledStop)
        self.assertFalse(self.voiceClient._calledPause)
        self.assertFalse(self.voiceClient._calledResume)

