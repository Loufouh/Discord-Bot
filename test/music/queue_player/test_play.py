from test.music.queue_player.test_case import TestCase

class TestQueuePlayer_play(TestCase):
    def testEmptyQueue(self):
        self.player.play(self.voiceClient)
        self.assert_not_playing()

    def testQueueWithOneSource(self):
        self.queue.add('source')

        self.player.play(self.voiceClient)
        self.assert_playing_source('source')

        self.voiceClient.stop()
        self.assertFalse(self.voiceClient.is_playing())

    def testQueueWithTwoSources(self):
        self.add_sources('source1', 'source2')
    
        self.player.play(self.voiceClient)
        self.assert_playing_source('source1')

        self.voiceClient.stop()
        self.assert_playing_source('source2')

        self.voiceClient.stop()
        self.assert_not_playing()

