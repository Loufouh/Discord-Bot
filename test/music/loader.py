import unittest
from music.loader import get_loader
from test.music.dummy_downloader import get_downloader

class TestMusicLoader(unittest.TestCase):
    downloader = get_downloader()
    loader = None

    def setUp(self):
        self.loader = get_loader()
        self.loader.downloader = self.downloader

        self.downloader.reset()

    def testLoad(self):
        source = self.loader.load_from_link('fakeLink')
        
        self.assertTrue(self.downloader.requestedDownload)
        self.assertEqual(self.downloader.lastLink, 'fakeLink')
        self.assertIsNotNone(source)

