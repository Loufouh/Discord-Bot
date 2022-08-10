import unittest

from dummies.commands.objects.command import Command_dummy
from dummies.context import Context_dummy

class TestCommand_execute(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.ctx = Context_dummy()
        self.command = Command_dummy()

    async def test_one_argument(self):
        await self.command.execute(self.ctx)

        self.assertTrue(self.command._hasBeenExecuted)

    async def test_two_arguments(self):
        await self.command.execute(self.ctx, 0)

        self.assertTrue(self.command._hasBeenExecuted)

    async def test_three_arguments(self):
        await self.command.execute(self.ctx, 0, 1)

        self.assertTrue(self.command._hasBeenExecuted)

    async def test_ten_arguments(self):
        await self.command.execute(self.ctx, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

        self.assertTrue(self.command._hasBeenExecuted)

