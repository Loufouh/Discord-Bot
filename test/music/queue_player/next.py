from test.music.queue_player.TestCase import TestCase

class TestQueuePlayer_next(TestCase):
    def testEmptyQueue(self):
        self.player.next()
        self.assert_not_playing()

    def testQueueWithThreeSources(self):
        self.add_sources('source1', 'source2', 'source3')

        self.player.play(self.voiceClient)
        self.player.next()
        self.assert_playing_source('source2')

        self.player.next()
        self.assert_playing_source('source3')

        self.player.next()
        self.assert_not_playing()

