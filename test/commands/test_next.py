import unittest

from commands.next import _next

from dummies.context import Context_dummy
from commands.objects.next import NextCommand
from commands.objects.command import get_command

class TestPlay(unittest.IsolatedAsyncioTestCase):
    async def test(self):
        ctx = Context_dummy()
        await _next(ctx)

        self.assertTrue(get_command(NextCommand)._hasBeenExecuted)

