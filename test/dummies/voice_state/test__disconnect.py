import unittest

from dummies.context import Context_dummy

class TestVoiceState__disconnect(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.ctx = Context_dummy()

        await self.ctx._connect_author()

        self.voiceState = self.ctx.author.voice

    async def test(self):
        await self.voiceState._disconnect()

        self.assertIsNone(self.ctx.author.voice)
        self.assertFalse(self.voiceState.channel.is_connected)

