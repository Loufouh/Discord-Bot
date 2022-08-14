import unittest

from music.queue import get_queue, Queue

class TestQueue_reset(unittest.TestCase):
    def test(self):
        queue = get_queue()

        queue.add('source')
        queue.reset()

        self.assertEqual(queue.get_size(), 0)

