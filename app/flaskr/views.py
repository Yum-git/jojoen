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

from .models import models_bunde

app = Flask(__name__)
cors = CORS(app, supports_credentials=True)
app.config["JSON_AS_ASCII"] = False


@app.route('/')
def index():
    """index.htmlの生成する関数"""
    return render_template('index.html')


@app.route('/api', methods=["GET", "POST"])
@cross_origin(supports_credentials=True) 
def make_text_to_music():
    """
    ユーザーが入力した文章を音楽, ワードクラウド画像に変換
    """
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
