from config import config

import unittest

from music.audio_url_retriever import AudioUrlRetriever

class TestAudioUrlRetriever_retrieve_from_link(unittest.TestCase):
    @unittest.skipIf(config['skipRequestTests'],
                    'To avoid spamming Youtube servers')
    def test(self):
        retriever = AudioUrlRetriever()

        url = retriever.retrieve_from_link('https://youtu.be/paveeT8QPXA')

        self.assertIn('mime=audio', url)
        
