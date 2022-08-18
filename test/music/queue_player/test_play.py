from test.music.queue_player.test_case import TestCase

class TestQueuePlayer_play(TestCase):
    def testEmptyQueue(self):
        self.player.play(self.voiceClient)
        self.assert_not_playing()

    def testQueueWithOneSource(self):
        self.queue.add(self.sources[0])

        self.player.play(self.voiceClient)
        self.assert_playing_source(self.sources[0])

        self.voiceClient.stop()
        self.assertFalse(self.voiceClient.is_playing())

    def testQueueWithTwoSources(self):
        self.add_sources(self.sources[0], self.sources[1])
    
        self.player.play(self.voiceClient)
        self.assert_playing_source(self.sources[0])

        self.voiceClient.stop()
        self.assert_playing_source(self.sources[1])

        self.voiceClient.stop()
        self.assert_not_playing()

