from os import path
import youtube_dl

def download(link, testing=False):
    info = get_info_from_link(link)
    options = generate_options_from_info(info, testing=testing)

    if not path.exists(options['outtmpl']):
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([info['webpage_url']])

    return options['outtmpl']

def get_info_from_link(link):
    return youtube_dl.YoutubeDL().extract_info(
            url=link,
            download=False
    )

def generate_options_from_info(info, testing=False):
    return {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': 'music_files/' + info['title'] + '.mp3',
        'test': testing,
        'live': True
    }   

