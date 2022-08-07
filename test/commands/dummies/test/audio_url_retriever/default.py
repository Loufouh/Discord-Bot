import unittest

from test.commands.dummies.audio_url_retriever import AudioUrlRetriever_dummy

class TestAudioUrlRetriever_default(unittest.TestCase):
    def test(self):
        retriever = AudioUrlRetriever_dummy()
        
        self.assertEqual(retriever._retrievedLink, '')
        self.assertFalse(retriever._triggerWrongUrlException)

