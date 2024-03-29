import unittest

from dummies.context import Context_dummy
from commands.join import _join
from commands.objects.join import JoinCommand
from commands.objects.command import get_command

class TestJoin(unittest.IsolatedAsyncioTestCase):
    async def test(self):
        ctx = Context_dummy()

        await _join(ctx)

        self.assertTrue(get_command(JoinCommand)._hasBeenExecuted)

