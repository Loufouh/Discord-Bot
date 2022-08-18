import unittest

from dummies.audio_url_retriever import AudioUrlRetriever_dummy

class TestAudioUrlRetriever_default(unittest.TestCase):
    def setUp(self):
        self.retriever = AudioUrlRetriever_dummy()

    def test(self):
        self.assertEqual(self.retriever._retrievedLink, '')
        self.assertFalse(self.retriever._triggerWrongUrlException)

