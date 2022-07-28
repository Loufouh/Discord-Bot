import unittest

from music.queue import Queue

class TestQueue(unittest.TestCase):
    queue = None

    def setUp(self):
        self.queue = Queue()

    def testEmpty(self):
        self.assertIsNone(self.queue.get_head())
        self.assertIsNone(self.queue.pop())

    def testAdd(self):
        self.queue.add('source1')

        self.assertEqual(self.queue.get_head(), 'source1')

    def testPop(self):
        self.queue.add('source1')
        self.queue.add('source2')
        self.queue.add('source3')

        self.assertEqual(self.queue.pop(), 'source1')
        self.assertEqual(self.queue.get_head(), 'source2')
        self.assertEqual(self.queue.pop(), 'source2')
        self.assertEqual(self.queue.get_head(), 'source3')
        self.assertEqual(self.queue.pop(), 'source3')

        self.assertIsNone(self.queue.get_head())
        self.assertIsNone(self.queue.pop())

