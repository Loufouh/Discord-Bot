import unittest
import discord

from music.ffmpeg_handler import FFmpegHandler

class TestFFmpegHandler_create_audio_from_url(unittest.TestCase):
    def test(self):
        handler = FFmpegHandler()

        audio = handler.create_audio_from_url('https://upload.wikimedia.org/wikipedia/commons/4/47/Beethoven_Moonlight_2nd_movement.ogg')

        self.assertIsInstance(audio, discord.AudioSource)

