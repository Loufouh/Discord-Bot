from test.dummies.context.test_case import TestCase
from dummies.voice_state import VoiceState_dummy

class TestContext__connect_author(TestCase):
    async def test(self):
        await self.ctx._connect_author()

        self.assertIsInstance(self.ctx.author.voice, VoiceState_dummy)

