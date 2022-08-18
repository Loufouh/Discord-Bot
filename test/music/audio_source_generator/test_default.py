import unittest

from music.audio_source_generator.common import AudioSourceGenerator
from music.audio_url_retriever import AudioUrlRetriever

class TestAudioSourceGenerator_default(unittest.TestCase):
    def setUp(self):
        self.generator = AudioSourceGenerator()

    def test(self):
        self.assertIsInstance(self.generator.urlRetriever, AudioUrlRetriever)

