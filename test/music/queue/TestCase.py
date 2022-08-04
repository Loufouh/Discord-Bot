import unittest

from music.queue import Queue

class TestCase(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def add_sources(self, sources):
        for source in sources:
            self.queue.add(source)

    def assert_pop_sequence(self, sequence):
        for source in sequence:
            self.assert_pop(source)

    def assert_pop(self, source):
        self.assertEqual(self.queue.pop(), source)

    def assert_head(self, source):
        self.assertEqual(self.queue.get_head(), source)

