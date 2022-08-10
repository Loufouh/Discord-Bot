import unittest

from commands.leave import _leave
from commands.objects.command import get_command
from commands.objects.leave import LeaveCommand

from dummies.context import Context_dummy

class TestLeave(unittest.IsolatedAsyncioTestCase):
    async def test(self):
        ctx = Context_dummy()

        await _leave(ctx)

        self.assertTrue(get_command(LeaveCommand)._hasBeenExecuted)
        
