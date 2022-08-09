from test.music.queue.TestCase import TestCase

class TestQueue_pop(TestCase):
    def test(self):
        self.add_sources(['source1', 'source2', 'source3'])

        self.assert_pop('source1')

        self.assert_head('source2')
        self.assert_pop('source2')

        self.assert_head('source3')
        self.assert_pop('source3')

        self.assert_head(None)
        self.assert_pop(None)

