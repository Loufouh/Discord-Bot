from test.music.downloader.TestCase import TestCase

class TestDownloader_download(TestCase):
    def test_download(self):
        self.download()

        self.assert_filename_right()
        self.assert_file_created()
    
    def test_download_twice(self):
        self.download()
        self.download()

        self.assert_filename_right()
        self.assert_file_created()

