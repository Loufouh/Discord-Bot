import unittest

from test.commands.context_dummy import Context_dummy
from commands.join import _join, AuthorNotConnectedException

class TestJoin(unittest.IsolatedAsyncioTestCase):
    ctx = None
    
    def setUp(self):
        self.ctx = Context_dummy()
        pass 

    async def test_author_not_connected(self):
        await _join(self.ctx)

        self.assertEqual(self.ctx.sent, 'Je trouve pas ton salon audio [mention]')

