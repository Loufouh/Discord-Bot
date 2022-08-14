import unittest

from music.queue import get_queue, Queue

class TestQueue_get_queue(unittest.TestCase):
    def test_once(self):
        queue = get_queue()

        self.assertIsInstance(queue, Queue)

    def test_twice(self):
        queue1 = get_queue()
        queue2 = get_queue()

        self.assertEqual(queue1, queue2)

