import unittest
import os

from music.downloader import get_downloader

class TestCase(unittest.TestCase):
    link = 'https://youtu.be/AhCYyopTPO0'
    expectedFilename = 'music_files/Ranch.mp3'
    givenFilename = ''

    downloader = None

    def setUp(self):
        self.downloader = get_downloader()
        self.remove_file()

    def tearDown(self):
        self.remove_file()

    def download(self):
        self.givenFilename = self.downloader.download_from_link(self.link)

    def remove_file(self):
        if os.path.exists(self.expectedFilename):
            os.remove(self.expectedFilename)

    def assert_all_right(self, filename):
        self.assert_filename_right()
        self.assert_file_created()

    def assert_filename_right(self):
        self.assertEqual(
            self.givenFilename,
            self.expectedFilename
        )

    def assert_file_created(self):
        self.assertTrue(
            os.path.exists(self.expectedFilename)
        )

