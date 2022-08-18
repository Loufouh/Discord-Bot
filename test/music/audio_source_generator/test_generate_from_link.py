import unittest
import discord

from music.audio_source_generator.common import AudioSourceGenerator, WrongLinkException

from dummies.audio_url_retriever import AudioUrlRetriever_dummy
from dummies.ffmpeg_handler import FFmpegHandler_dummy

class TestAudioSourceGenerator_generate_from_link(unittest.TestCase):
    def setUp(self):
        self.generator = AudioSourceGenerator()
        self.generator.urlRetriever = AudioUrlRetriever_dummy()
        self.generator.ffmpegHandler = FFmpegHandler_dummy()

    def test(self):
        source = self.generator.generate_from_link('fake_link')

        self.assertIsInstance(source, discord.AudioSource)

    def test_wrong_link(self):
        self.generator.urlRetriever._triggerWrongUrlException = True

        with self.assertRaises(WrongLinkException):
            self.generator.generate_from_link('wrong_link')

