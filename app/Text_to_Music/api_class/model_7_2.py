# base64形式の音楽と画像を返す
class returnbase64(object):
    def __init__(self, music, picture=None):
        self.music = music
        self.picture = picture
        
    def json_data_back(self):
        return self.music, self.picture