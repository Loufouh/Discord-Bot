import unittest
from music.audio_url_retriever import get_retriever

class TestAudioURLRetriever_retrieve(unittest.TestCase):
    def test(self):
        retriever = get_retriever()

        youtubeURL = 'https://youtu.be/paveeT8QPXA'

        self.assertTrue('mime=audio' in retriever.retrieve(youtubeURL)) 
        
