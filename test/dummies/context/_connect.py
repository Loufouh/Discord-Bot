import unittest

from dummies.context import Context_dummy
from commands.exceptions.exceptions import AuthorNotConnectedException

class TestContext__connect(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.ctx = Context_dummy()

    async def test_normal(self):
        await self.ctx._connect_author()
        await self.ctx._connect()

        self.assertTrue(self.ctx.author.voice.channel._isConnected)

    async def test_author_not_connected(self):
        with self.assertRaises(AuthorNotConnectedException):
            await self.ctx._connect()

        self.assertIsNone(self.ctx.author.voice)

