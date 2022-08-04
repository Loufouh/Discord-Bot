import subprocess

class WrongUrlException(Exception):
    pass

class Retriever:
    def retrieve(self, youtube_url):
        result = subprocess.run(
            ['youtube-dl', '-f', 'bestaudio/best', '--get-url', youtube_url],
            stdout=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            raise WrongUrlException()

        return result.stdout

retriever = None

def get_retriever():
    global retriever

    if retriever is None:
        retriever = Retriever()

    return retriever
