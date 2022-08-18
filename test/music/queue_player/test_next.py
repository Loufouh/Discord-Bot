from test.music.queue_player.test_case import TestCase

class TestQueuePlayer_next(TestCase):
    def testEmptyQueue(self):
        self.player.next()
        self.assert_not_playing()

    def testQueueWithThreeSources(self):
        self.add_sources(self.sources[0], self.sources[1], self.sources[2])

        self.player.play(self.voiceClient)
        self.player.next()
        self.assert_playing_source(self.sources[1])

        self.player.next()
        self.assert_playing_source(self.sources[2])

        self.player.next()
        self.assert_not_playing()

