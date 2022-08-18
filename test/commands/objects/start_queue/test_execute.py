from test.commands.objects.start_queue.test_case_execute import TestCase

from music.queue import get_queue

class TestStartQueueCommand_execute(TestCase):
    async def test_normal(self):
        await self.command.execute(self.ctx)

        self.assertTrue(self.player._calledPlay)
        self.assertEqual(self.player.voiceClient, self.ctx.voice_client)
        self.assertEqual(self.player.queue, get_queue())
        self.assertEqual(self.ctx.sent, 'C\'est parti ! [author.mention]')

    async def test_author_not_connected(self):
        await self.ctx._disconnect_author()

        await self.command.execute(self.ctx)

        self.assertEqual(self.ctx.sent, 'Tu dois être connecté à un salon audio pour ça [author.mention]')

    async def test_not_connected(self):
        await self.ctx._disconnect()

        await self.command.execute(self.ctx)

        self.assertEqual(self.ctx.sent, 'Je suis pas connecté au salon [author.mention]')

    async def test_empty_queue(self):
        get_queue().reset()

        await self.command.execute(self.ctx)

        self.assertEqual(self.ctx.sent, 'La file est vide [author.mention]')

