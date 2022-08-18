from test.music.queue.test_case import TestCase

class TestQueue_pop(TestCase):
	def test_simple(self):
		self.queue.add('source')
		self.assert_pop('source')

	def test_normal(self):
		self.add_sources(['source1', 'source2', 'source3'])

		self.assert_pop('source1')
		self.assert_pop('source2')
		self.assert_pop('source3')

		self.assert_pop(None)

	def test_empty(self):
		self.assert_pop(None)

