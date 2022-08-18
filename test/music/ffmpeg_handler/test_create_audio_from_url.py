import unittest
import discord

from music.ffmpeg_handler import FFmpegHandler

class TestFFmpegHandler_create_audio_from_url(unittest.TestCase):
    def setUp(self):
        self.handler = FFmpegHandler()
        self.link = 'https://upload.wikimedia.org/wikipedia/commons/4/47/Beethoven_Moonlight_2nd_movement.ogg'

    def test(self):
        audio = self.handler.create_audio_from_url(self.link)

        self.assertIsInstance(audio, discord.AudioSource)

