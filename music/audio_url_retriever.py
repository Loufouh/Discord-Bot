import subprocess

class WrongUrlException(Exception):
    pass

class AudioUrlRetriever:
    def retrieve(self, youtube_url):
        result = subprocess.run(
            ['youtube-dl', '--quiet', '-f', 'bestaudio/best', '--get-url', youtube_url],
            stdout=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            raise WrongUrlException()

        return result.stdout

