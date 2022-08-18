from test.dummies.context.test_case import TestCase
from dummies.author import Author_dummy

class TestContext_default(TestCase):
    def test(self):
        self.assertIsInstance(self.ctx.author, Author_dummy)
        self.assertIsNone(self.ctx.voice_client)
        self.assertEqual(self.ctx.sent, '')

