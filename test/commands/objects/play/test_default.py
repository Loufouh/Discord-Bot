import unittest

from commands.objects.play import PlayCommand
from music.audio_source_generator.common import AudioSourceGenerator

class TestPlayCommand_default(unittest.TestCase):
    def test(self):
        command = PlayCommand()
        
        self.assertIsInstance(command.sourceGenerator, AudioSourceGenerator)

