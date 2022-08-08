import unittest

from test.commands.dummies.context import Context_dummy
from dummies.author import Author_dummy

class TestContext_default(unittest.TestCase):
    def setUp(self):
        self.context = Context_dummy()

    def test(self):
        self.assertIsInstance(self.context.author, Author_dummy)
        self.assertIsNone(self.context.voice_client)
        self.assertEqual(self.context.sent, '')

