import unittest

from dummies.context import Context_dummy
from message_sender import MessageSender

class TestMessageSender_send(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.ctx = Context_dummy()
        self.sender = MessageSender(self.ctx)

    async def test_no_mentionning(self):
        self.sender.mentionningActivated = False

        await self.sender.send('Test message')

        self.assertEqual(self.ctx.sent, 'Test message')

    async def test_mentionning(self):
        await self.sender.send('Test message')

        self.assertEqual(self.ctx.sent, 'Test message [author.mention]')

