from config import config

import unittest

from music.audio_url_retriever import get_retriever

class TestAudioURLRetriever_retrieve(unittest.TestCase):
    @unittest.skipIf(config['skipRequestTests'],
                    'To avoid spamming Youtube servers')
    def test(self):
        youtubeURL = 'https://youtu.be/paveeT8QPXA'
        url = get_retriever().retrieve(youtubeURL)

        self.assertIn('mime=audio', url)
        
