import model_3, model_4, model_7_1, model_7_2
import model_music1, model_music2, model_music3, model_music4

class StartClass(object):
    def __init__(self, input):
        # 1. 何かしらを入力を受け付ける
        self.input_object = input
        self.audio_path = '../tmp/audio.wav'
        self.picture_path = '../tmp/word.png'

        self.audio_binary = None
        self.picture_binary = None
    
    def main_(self):
        # 2. 入力した文字列をローマ字に変換する
        textConveter = model_music1.converter(self.input_object)
        lastText = textConveter.convertText()

        # ポジネガ判定　後で実装
        PosiNegaScore = 3

        # 5. ローマ字を元にドレミに変換する
        musicConveter = model_music2.musicalConverter(lastText)
        musicalScore = musicConveter.convertMusic
        
        # リズムをつくる
        makeRhythm = model_music3.makeRhythm(PosiNegaScore, musicalScore)
        makeRhythm.rhythm()
        melody = makeRhythm.melody()

        # 6. ドレミを音声に変換する
        rec = Recorder(PosiNegaScore, melody)
        rec.save(self.audio_path)

        # 3. 入力した文字列を形態素解析で単語化
        model_3_class = model_3.ChangeWord(self.input_object)
        word_lists = model_3_class.main_("名詞") 

        # 4. 分割した単語から図を生成
        model_4_class = model_4.WordChange(word_lists)
        self.picture_path = model_4_class.Picture_create()

        # 7. base64にしてjson形式に変換
        ## 7_1. base64に変換
        ### audiobinary
        model_7_1_class = model_7_1.changebase64(self.audio_path)
        self.audio_binary = model_7_1_class.change()

        ### picturebinary
        model_7_1_class.__changepath__(self.picture_path)
        self.picture_binary = model_7_1_class.change()

        ## 7_2. base64をreturn
        return self.audio_binary, self.picture_binary
