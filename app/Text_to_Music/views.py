from django.shortcuts import render
from .models import ReturnMusicFile
from rest_framework import viewsets, filters
from .serializers import MusicSerializer

from .in_class import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

class MusicView(viewsets.ModelViewSet):
    queryset = ReturnMusicFile.objects.all()
    serializer_class = MusicSerializer

    # 