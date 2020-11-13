from django.urls import path

from .views import index, MusicView

urlpatterns = [
    path('', index),
    path('api/', MusicView.as_view())
]