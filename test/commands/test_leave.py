import unittest

from commands.leave import _leave
from commands.objects.leave import get_command

from dummies.context import Context_dummy

class TestLeave(unittest.IsolatedAsyncioTestCase):
    async def test(self):
        ctx = Context_dummy()

        await _leave(ctx)

        self.assertTrue(get_command()._hasBeenExecuted)
        
