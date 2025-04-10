from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.downloader import baixar_video_yt
import os

app = FastAPI()

class VideoRequest(BaseModel):
    url: str

@app.post("/baixar")
def baixar(req: VideoRequest, background_tasks: BackgroundTasks):
    try:
        path, filename = baixar_video_yt(req.url)
        background_tasks.add_task(os.remove, path)
        return FileResponse(path, media_type="video/mp4", filename=filename)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
