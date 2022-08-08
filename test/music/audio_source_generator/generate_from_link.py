import unittest
import discord

from music.audio_source_generator import AudioSourceGenerator

from test.commands.dummies.audio_url_retriever import AudioUrlRetriever_dummy
from test.commands.dummies.ffmpeg_handler import FFmpegHandler_dummy

class TestAudioSourceGenerator_generate_from_link(unittest.TestCase):
    def setUp(self):
        self.generator = AudioSourceGenerator()
        self.generator.urlRetriever = AudioUrlRetriever_dummy()
        self.generator.ffmpegHandler = FFmpegHandler_dummy()

    def test(self):
        source = self.generator.generate_from_link('fake_link')

        self.assertIsInstance(source, discord.AudioSource)

