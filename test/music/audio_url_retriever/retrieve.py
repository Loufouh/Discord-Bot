from config import config

import unittest

from music.audio_url_retriever import AudioUrlRetriever

class TestAudioUrlRetriever_retrieve(unittest.TestCase):
    @unittest.skipIf(config['skipRequestTests'],
                    'To avoid spamming Youtube servers')
    def test(self):
        retriever = AudioUrlRetriever()

        url = retriever.retrieve('https://youtu.be/paveeT8QPXA')

        self.assertIn('mime=audio', url)
        
