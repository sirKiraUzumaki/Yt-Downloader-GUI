import youtube_dl
from tkinter import messagebox


def errorGUI(str):
    messagebox.showerror('Error', str)
    
def info(str):
    messagebox.showinfo('Info', str)
    
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)
        errorGUI(msg)


def my_hook(d):
    if d['status'] == 'finished':
        info('Done Downloading!!')
        print('Done downloading, now converting ...')


mp3_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

mp4_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'
}

def mp3(link):
    info('Download has been started!')
    with youtube_dl.YoutubeDL(mp3_opts) as ydl:
        ydl.download([link])
        print(MyLogger)
 
def mp4(link):
    info('Download has been started!')
    with youtube_dl.YoutubeDL(mp4_opts) as ydl:
        ydl.download([link])
        print(MyLogger)
 
def vidInfo(link):
    ydl = youtube_dl.YoutubeDL({'skip_download': True, 'noplaylist': True})
    info = ydl.extract_info(link, download=False)
    vidData = {
        'id': info['id'],
        'title': info['title'],
        'thumbnail': info['thumbnail']
    }
    print(info)
    return vidData
mp4('https://www.youtube.com/_hBswwpLAkY')