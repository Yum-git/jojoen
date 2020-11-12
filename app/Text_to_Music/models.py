from django.db import models

# Create your models here.

class ReturnMusicFile(models.Model):
    music_base64 = models.TextField()
    picture_base64 = models.TextField()
    