import yt_dlp
import os
import uuid
from app.config import DOWNLOAD_DIR, MAX_DURATION, MAX_FILESIZE

def baixar_video_yt(url: str):
    video_id = str(uuid.uuid4())
    output_template = os.path.join(DOWNLOAD_DIR, f"{video_id}-%(title)s.%(ext)s")

    # Salva os cookies num arquivo temporário
    cookie_text = os.environ.get("YT_COOKIES")
    cookie_path = "cookies.txt"

    if cookie_text:
        with open(cookie_path, "w", encoding="utf-8") as f:
            f.write(cookie_text)

    ydl_opts = {
        'format': 'bestvideo[height=1080][fps<=30][vcodec*=avc1][ext=mp4]+bestaudio[acodec*=mp4a][ext=m4a]/best[ext=mp4]',
        'merge_output_format': 'mp4',
        'outtmpl': output_template,
        'quiet': True,
        'cookiefile': cookie_path,
        'noplaylist': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        duration = info.get("duration", 0)
        filesize = info.get("filesize_approx", 0)

        if duration > MAX_DURATION:
            raise ValueError("Vídeo excede a duração máxima permitida (10 minutos).")
        if filesize and filesize > MAX_FILESIZE:
            raise ValueError("Vídeo excede o tamanho máximo permitido (200 MB).")

        ydl.download([url])

    title = info.get("title", "video")
    filename = f"{title}.mp4"
    full_path = os.path.join(DOWNLOAD_DIR, f"{video_id}-{title}.mp4")

    return full_path, filename
