import unittest

from test.commands.dummies.context import Context_dummy

class TestContext__disconnect(unittest.IsolatedAsyncioTestCase):
    async def test(self):
        ctx = Context_dummy()

        await ctx._connect_author()
        await ctx._connect()

        await ctx._disconnect()

        self.assertIsNone(ctx.voice_client)

