from . import PosiNega, MusicConverter, MakeRhythm, Recorder, ChangeWord, WordChange, ChangeBase64


class StartClass(object):
    def __init__(self, input_sentence: str):
        # 1. 何かしらを入力を受け付ける
        self.input_object = input_sentence
        self.audio_path = '../tmp/audio.wav'
        self.picture_path = '../tmp/word.png'

        self.audio_binary = None
        self.picture_binary = None

    def main_(self):
        # 3. ポジネガ判定
        judge = PosiNega.PosiNega(self.input_object)
        posinega_score, tangonum = judge.posi_nega_jud()

        # 4. ローマ字を元にドレミに変換する
        music_conveter = MusicConverter.musicalConverter(posinega_score)
        musical_score = music_conveter.convertMusic()

        # 5. リズムをつくる
        make_rhythm = MakeRhythm.makeRhythm(posinega_score, musical_score)
        make_rhythm.rhythmMake()
        melody = make_rhythm.melodyMake()

        # 6. ドレミを音声に変換する
        rec = Recorder.Recorder(posinega_score, melody)
        rec.save(self.audio_path)

        # 7. 入力した文字列を形態素解析で単語化
        change_word_class = ChangeWord.ChangeWord(self.input_object)
        word_lists = change_word_class.main_("名詞")

        # 8. 分割した単語から図を生成
        word_change_class = WordChange.WordChange(word_lists, posinega_score)
        self.picture_path = word_change_class.Picture_create()

        if self.picture_path is False:
            return 'None', 'None', 203

        # 8. base64にしてjson形式に変換
        # 8_1. base64に変換
        # 8_1_1. 音楽
        change_base64_class = ChangeBase64.changebase64(self.audio_path)
        self.audio_binary = change_base64_class.change()

        # 8_1_2. 写真
        change_base64_class.__changepath__(self.picture_path)
        self.picture_binary = change_base64_class.change()

        # 8_2. base64をreturn
        return self.audio_binary, self.picture_binary, 200
