from test.music.queue.test_case import TestCase

class TestQueue_get_head(TestCase):
	def test_simple(self):
		self.queue.add('source')
		self.assert_head('source')
	
	def test_with_popping(self):
		self.add_sources(['source1', 'source2', 'source3'])

		self.assert_head('source1')
		self.queue.pop()
		self.assert_head('source2')
		self.queue.pop()
		self.assert_head('source3')
		self.queue.pop()
		self.assert_head(None)

	def test_empty(self):
		self.assert_head(None)

