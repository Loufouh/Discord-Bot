import unittest

from dummies.context import Context_dummy

from commands.objects.leave import LeaveCommand

class TestLeaveCommand_execute(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.ctx = Context_dummy()
        self.command = LeaveCommand()

    async def test_normal(self):
        await self.ctx._connect_author()
        await self.ctx._connect()

        await self.command.execute(self.ctx)

        self.assertEqual(self.ctx.replied, 'Bye !')
        self.assertIsNone(self.ctx.voice_client)

    async def test_not_connected(self):
        await self.command.execute(self.ctx)

        self.assertEqual(self.ctx.replied, 'Chuis pas connecté')

