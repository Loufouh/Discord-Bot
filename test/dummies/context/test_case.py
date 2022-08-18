import unittest

from dummies.context import Context_dummy

class TestCase(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.ctx = Context_dummy()

