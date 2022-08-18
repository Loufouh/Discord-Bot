import unittest

from music.audio_source_generator.common import AudioSourceGenerator
from music.audio_url_retriever import AudioUrlRetriever

class TestAudioSourceGenerator_default(unittest.TestCase):
    def test(self):
        generator = AudioSourceGenerator()

        self.assertIsInstance(generator.urlRetriever, AudioUrlRetriever)

