from test.music.queue.TestCase import TestCase

class TestQueue_add(TestCase):
    def testAddOnce(self):
        self.queue.add('source1')
        self.assert_head('source1')

    def testAddTwice(self):
        self.queue.add('source1')
        self.queue.add('source2')

        self.assert_head('source1')

    def testContinuousAdd(self):
        self.add_sources(['source1', 'source2'])
        self.assert_pop('source1')

        self.add_sources(['source3', 'source4'])
        self.assert_pop('source2')

        self.queue.add('source5')
        self.assert_pop_sequence(['source3', 'source4', 'source5'])

        self.assert_head(None)
        self.assert_pop(None)

