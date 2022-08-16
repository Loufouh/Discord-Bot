import unittest

from dummies.context import Context_dummy

class TestContext__disconnect_author(unittest.IsolatedAsyncioTestCase):
    async def test(self):
        ctx = Context_dummy()

        await ctx._connect_author()

        await ctx._disconnect_author()

        self.assertIsNone(ctx.author.voice)

