from test.music.queue.TestCase import TestCase

class TestQueue_pop(TestCase):
    def test_empty(self):
        self.assertEqual(self.queue.get_size(), 0)
    
    def test_one_source(self):
        self.queue.add('source')

        self.assertEqual(self.queue.get_size(), 1)

    def test_100_sources(self):
        self.add_sources(['source']*100)

        self.assertEqual(self.queue.get_size(), 100)

