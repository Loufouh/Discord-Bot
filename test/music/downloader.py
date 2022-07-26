import unittest
import os

from music.downloader import get_downloader

class TestDownloader(unittest.TestCase):
    link = 'https://youtu.be/AhCYyopTPO0'
    expectedFilename = 'music_files/Ranch.mp3'
    givenFilename = ''

    downloader = None

    def setUp(self):
        self.downloader = get_downloader()
        self.removeFile()

    def tearDown(self):
        self.removeFile()

    def test_download(self):
        self.download()

        self.assertFilenameRight()
        self.assertFileCreated()
    
    def test_download_twice(self):
        self.download()
        self.download()

        self.assertFilenameRight()
        self.assertFileCreated()


    def download(self):
        self.givenFilename = self.downloader.download_from_link(self.link)

    def removeFile(self):
        if os.path.exists(self.expectedFilename):
            os.remove(self.expectedFilename)

    def assertAllRight(self, filename):
        self.assertFilenameRight()
        self.assertFileCreated()

    def assertFilenameRight(self):
        self.assertEqual(
                self.givenFilename,
                self.expectedFilename
            )

    def assertFileCreated(self):
        self.assertTrue(
                os.path.exists(self.expectedFilename)
            )

