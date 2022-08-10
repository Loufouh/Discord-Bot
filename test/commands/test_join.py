import unittest

from dummies.context import Context_dummy
from dummies.voice_state import VoiceState_dummy

from commands.join import _join, AuthorNotConnectedException

class TestJoin(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.ctx = Context_dummy()

    async def test_author_not_connected(self):
        await _join(self.ctx)

        self.assert_sent_channel_not_found()

    async def test_already_connected(self):
        await self.ctx._connect_author()
        await self.ctx._connect()

        await _join(self.ctx)
        
        self.assert_sent_already_connected()
        self.assert_connected_to_channel()

    async def test_normal(self):
        await self.ctx._connect_author()

        await _join(self.ctx)

        self.assert_sent_joining_message()
        self.assert_connected_to_channel()

    def assert_sent_channel_not_found(self):
        self.assertEqual(self.ctx.sent, 'Je trouve pas ton salon audio [author.mention]')

    def assert_sent_already_connected(self):
        self.assertEqual(self.ctx.sent, 'Je suis déjà connecté [author.mention]') 

    def assert_sent_joining_message(self):
        self.assertEqual(self.ctx.sent, 'J\'arrive [author.mention] !')

    def assert_connected_to_channel(self):
        self.assertTrue(self.ctx.author.voice.channel._isConnected)

