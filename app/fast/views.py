from .models import models_bundle

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI()
templates = Jinja2Templates(directory="fast/templates")
app.mount("/static", StaticFiles(directory="fast/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/api")
async def make_text_to_music(sentence: str):
    api_start = models_bundle.StartClass(sentence)
    audio, picture, status_ = api_start.main_()

    return {"audio": audio, "picture": picture}

