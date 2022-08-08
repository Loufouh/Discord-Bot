import unittest
import discord

from test.commands.dummies.audio_source_generator import AudioSourceGenerator_dummy
from test.commands.dummies.audio_url_retriever import AudioUrlRetriever_dummy
from test.commands.dummies.ffmpeg_handler import FFmpegHandler_dummy

class TestAudioSourceGenerator_default(unittest.TestCase):
    def test(self):
        generator = AudioSourceGenerator_dummy()

        self.assertIsInstance(generator.urlRetriever, AudioUrlRetriever_dummy)
        self.assertIsInstance(generator.ffmpegHandler, FFmpegHandler_dummy)

