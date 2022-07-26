import unittest
from sys import path

from src.music.downloader.downloader import get_downloader

class TestDownloader(unittest.TestCase):
    def test_download(self):
        filename = get_downloader().download('https://youtu.be/AhCYyopTPO0')

        self.assertEqual(filename, 'music_files/Ranch.mp3')
        self.assertTrue(path.exists('music_files/Ranch.mp3'))

