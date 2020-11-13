import base64

# 音楽（・画像）をbase64に変換する
class changebase64(object):
    def __init__(self, file_path):
        self.output_path = file_path

    def __changepath__(self, file_path):
        self.output_path = file_path
    
    def change(self):
        with open(self.output_path, "rb") as f:
            binary_data = base64.b64encode(f.read()).decode('utf-8')
        
        return binary_data