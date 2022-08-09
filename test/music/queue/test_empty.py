from test.music.queue.TestCase import TestCase

class TestQueue_empty(TestCase):
    def testEmpty(self):
        self.assert_head(None)
        self.assert_pop_sequence([None])
 
