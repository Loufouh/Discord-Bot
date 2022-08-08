import unittest
import discord

from music.audio_source_generator import WrongLinkException
from dummies.audio_source_generator import AudioSourceGenerator_dummy

class TestAudioSourceGenerator_generate_from_link(unittest.TestCase):
    def setUp(self):
        self.generator = AudioSourceGenerator_dummy()

    def test(self):
        source = self.generator.generate_from_link('fake_link')

        self.assertIsInstance(source, discord.AudioSource)

    def test_wrong_link(self):
        self.generator.triggerWrongLinkException = True

        with self.assertRaises(WrongLinkException):
            self.generator.generate_from_link('wrong_link')

