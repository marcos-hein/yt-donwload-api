# API YouTube Downloader

API simples para baixar vídeos do YouTube em 1080p com áudio, usando FastAPI e yt-dlp.

### Endpoints

- `POST /baixar` — envia JSON com o link do vídeo:
```json
{
  "url": "https://youtube.com/..."
}
```
### Install Dependencies
```
python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

```

### Run
```bash
uvicorn app.main:app --reload --port 5000
```