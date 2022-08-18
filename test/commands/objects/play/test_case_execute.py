import unittest

from commands.objects.play import PlayCommand

from dummies.context import Context_dummy
from dummies.audio_source_generator import AudioSourceGenerator_dummy

class TestCase(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.command = PlayCommand()

        self.command.sourceGenerator = AudioSourceGenerator_dummy()
        self.ctx = Context_dummy()

        await self.ctx._connect_author()
        await self.ctx._connect()

