import unittest

from commands.objects.add import AddCommand
from music.audio_source_generator.common import AudioSourceGenerator

class TestAddCommand_default(unittest.TestCase):
    def test(self):
        command = AddCommand()
        
        self.assertIsInstance(command.sourceGenerator, AudioSourceGenerator)

