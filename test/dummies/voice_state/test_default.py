import unittest

from dummies.voice_state import VoiceState_dummy
from dummies.context import Context_dummy
from dummies.channel import Channel_dummy

class TestVoiceState_default(unittest.TestCase):
    def setUp(self):
        self.ctx = Context_dummy()
        self.voiceState = VoiceState_dummy(self.ctx)

    def test(self):
        self.assertEqual(self.voiceState.ctx, self.ctx)
        self.assertIsInstance(self.voiceState.channel, Channel_dummy)

