from config import config

import unittest

from music.audio_url_retriever import get_retriever

class TestAudioURLRetriever_retrieve(unittest.TestCase):
    @unittest.skipIf(config['skipRequestTests'],
                    'Avoid spamming Youtube servers')
    def test(self):
        retriever = get_retriever()

        youtubeURL = 'https://youtu.be/paveeT8QPXA'

        self.assertTrue('mime=audio' in retriever.retrieve(youtubeURL)) 
        
