import unittest
import discord

from dummies.ffmpeg_handler import FFmpegHandler_dummy

class TestFFmpegHandler_create_from_url(unittest.TestCase):
    def test(self):
        handler = FFmpegHandler_dummy()

        audio = handler.create_audio_from_url('random_fake_url')

        self.assertIsInstance(audio, discord.AudioSource)

