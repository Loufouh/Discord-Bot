from test.dummies.context.test_case import TestCase
from dummies.voice_client import VoiceClient_dummy
from commands.exceptions.exceptions import AuthorNotConnectedException

class TestContext__connect(TestCase):
    async def test_normal(self):
        await self.ctx._connect_author()
        await self.ctx._connect()

        self.assertTrue(self.ctx.author.voice.channel._isConnected)
        self.assertIsInstance(self.ctx.voice_client, VoiceClient_dummy)

    async def test_author_not_connected(self):
        with self.assertRaises(AuthorNotConnectedException):
            await self.ctx._connect()

        self.assertIsNone(self.ctx.author.voice)

