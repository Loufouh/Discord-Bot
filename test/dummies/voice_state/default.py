import unittest

from test.commands.dummies.voice_state import VoiceState_dummy
from dummies.context import Context_dummy
from test.commands.dummies.channel import Channel_dummy

class TestVoiceState_default(unittest.TestCase):
    def test(self):
        ctx = Context_dummy()
        voiceState = VoiceState_dummy(ctx)

        self.assertEqual(voiceState.ctx, ctx)
        self.assertIsInstance(voiceState.channel, Channel_dummy)

