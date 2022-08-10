import unittest

from dummies.context import Context_dummy
from message_sender import MessageSender

class TestMessageSender_default(unittest.TestCase):
    def test(self):
        ctx = Context_dummy()
        sender = MessageSender(ctx)

        self.assertEqual(ctx, sender.ctx)
        self.assertTrue(sender.mentionningActivated)

