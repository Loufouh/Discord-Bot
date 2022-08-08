import unittest
import discord

from test.commands.dummies.audio_url_retriever import AudioUrlRetriever_dummy
from music.audio_url_retriever import WrongUrlException

class TestAudioUrlRetriever_retrieve(unittest.TestCase):
    def setUp(self):
        self.retriever = AudioUrlRetriever_dummy()

    def test_successful(self):
        url = self.retriever.retrieve_from_link('fake_link')

        self.assertEqual(url, 'fake_url')

    def test_WrongUrlException(self):
        self.retriever._triggerWrongUrlException = True

        with self.assertRaises(WrongUrlException):
            self.retriever.retrieve_from_link('fake_link')

