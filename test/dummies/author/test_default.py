import unittest

from dummies.author import Author_dummy

class TestAuthor_default(unittest.TestCase):
    def test(self):
        author = Author_dummy()
        self.assertIsNone(author.voice)
        self.assertEqual(author.mention, '[author.mention]')
        
