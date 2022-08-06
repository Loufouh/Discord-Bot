import unittest

from test.commands.dummies.voice_protocol import VoiceProtocol_dummy
from test.commands.dummies.context import Context_dummy

class TestVoiceProtocol_default(unittest.IsolatedAsyncioTestCase):
    def test(self):
        ctx = Context_dummy()
        voiceProtocol = VoiceProtocol_dummy(ctx)

        self.assertEqual(voiceProtocol.ctx, ctx)

