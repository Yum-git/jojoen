from flask import (
    jsonify,
    request,
    Flask,
    render_template,
    make_response
)
from flask_cors import (
    CORS, 
    cross_origin
)

from .models import models_bundle

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn

# app = Flask(__name__)
app = FastAPI()

# cors = CORS(app, supports_credentials=True)
# app.config["JSON_AS_ASCII"] = False
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

"""
@app.route('/')
@cross_origin(supports_credentials=True) 
def index():
	return render_template('index.html')
"""
@app.get("/")
async def index():
    return {"Hello": "World!"}

"""
@app.route('/api', methods=["GET", "POST"])
@cross_origin(supports_credentials=True) 
def make_text_to_music():
    sentence = request.args.get('sentence',"", type=str)
    print(f"mozi:{sentence}")
    # sentence = "あああがkfgぱf後じゃs歩g邪pdギアdw＠おふぁいf＠亜sファsfぱファsfか＠フォアpsd＠フォア＠fぱdf＠"
    api_start = models_bunde.StartClass(sentence)
    audio, picture, status_ = api_start.main_()

    return jsonify(
        {
            "audio": audio, 
            "picture": picture, 
        }
    ), status_
"""


@app.get("/api")
async def make_text_to_music():
    sentence = request.args.get('sentence',"", type=str)
    print(f"mozi:{sentence}")
    # sentence = "あああがkfgぱf後じゃs歩g邪pdギアdw＠おふぁいf＠亜sファsfぱファsfか＠フォアpsd＠フォア＠fぱdf＠"
    api_start = models_bundle.StartClass(sentence)
    audio, picture, status_ = api_start.main_()

    return {"audio": audio, "picture":picture}
