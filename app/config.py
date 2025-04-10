import os

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

MAX_DURATION = 10 * 60        # 10 minutos
MAX_FILESIZE = 200 * 1024 * 1024  # 200 MB
