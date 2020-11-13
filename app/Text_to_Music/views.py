from django.shortcuts import render
from .models import ReturnMusicFile
from rest_framework import viewsets, filters, generics
# from .serializers import MusicSerializer

# 実験用import
from rest_framework.response import Response
import json

# まとめフォルダ
from .api_class import models_bunde
# Create your views here.

def index(request):
    return render(request, 'index.html')

# とりあえず最低限の仕組みだけ作成
# djangorestframework　→　django+jsonで作成
class MusicView(generics.RetrieveAPIView):
    def post(self, request, format=None, output="test"):
        # フロントからjsonを受け取る
        output = json.loads(request.body)

        # json内部の文章を取得する
        sentence = output["sentence"]

        # 文章→写真・音楽に変換する
        api_start = models_bunde.StartClass(sentence)
        audio, picture = api_start.main_()
        
        # jsonにて返却する
        return Response(
            data={
                "music":audio,
                "picture":picture
            }
        )
