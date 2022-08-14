import unittest

from commands.add import _add

from dummies.context import Context_dummy
from commands.objects.add import AddCommand
from commands.objects.command import get_command

class TestAdd(unittest.IsolatedAsyncioTestCase):
    async def test(self):
        ctx = Context_dummy()
        await _add(ctx, 'fake_link')

        self.assertTrue(get_command(AddCommand)._hasBeenExecuted)

