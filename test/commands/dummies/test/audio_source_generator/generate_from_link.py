import unittest
import discord

from test.commands.dummies.audio_source_generator import AudioSourceGenerator_dummy

class TestAudioSourceGenerator_generate_from_link(unittest.TestCase):
    def test(self):
        generator = AudioSourceGenerator_dummy()

        source = generator.generate_from_link('fake_link')

        self.assertIsInstance(source, discord.AudioSource)

