import unittest

from dummies.context import Context_dummy
from dummies.voice_state import VoiceState_dummy

class TestContext__connect_author(unittest.IsolatedAsyncioTestCase):
    async def test(self):
        ctx = Context_dummy()

        await ctx._connect_author()

        self.assertIsInstance(ctx.author.voice, VoiceState_dummy)

