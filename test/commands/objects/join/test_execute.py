import unittest

from commands.objects.join import JoinCommand
from dummies.context import Context_dummy

class TestJoinCommand_execute(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.ctx = Context_dummy()
        self.command = JoinCommand()

    async def test_normal(self):
        await self.ctx._connect_author()

        await self.command.execute(self.ctx)

        self.assertEqual(self.ctx.replied, 'J\'arrive !')
        self.assertTrue(self.ctx.author.voice.channel._isConnected)

    async def test_author_not_connected(self):
        await self.command.execute(self.ctx)

        self.assertEqual(self.ctx.replied, 'Tu dois être connecté à un salon audio pour ça')

    async def test_already_connected(self):
        await self.ctx._connect_author()

        await self.command.execute(self.ctx)
        await self.command.execute(self.ctx)

        self.assertEqual(self.ctx.replied, 'Je suis déjà connecté') 
        self.assertTrue(self.ctx.author.voice.channel._isConnected)

