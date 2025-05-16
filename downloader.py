import yt_dlp

def download_media(url, media_type='video'):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
    }

    if media_type == 'audio':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        ydl_opts.update({
            'format': 'best',
        })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.download([url])
            return "Download complete."
    except Exception as e:
        return f"Error: {e}"
