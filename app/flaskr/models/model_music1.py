from pykakasi import kakasi


# 2. 入力した文字列をローマ字に変換する
class converter(object):

    def __init__(self, text, wav=None):
        self.text = text
        self.lastText = []

    def convertText(self):
        kakasi_ = kakasi()

        ####### 変換をset　　#######
        kakasi_.setMode('J', 'H')  # J(Kanji) to H(Hiragana)
        kakasi_.setMode('H', 'H')  # H(Hiragana) to None(noconversion)
        kakasi_.setMode('K', 'H')  # K(Katakana) to a(Hiragana)
        kakasi_.setMode('a', 'H')  # K(Katakana) to a(Hiragana)
        conv = kakasi_.getConverter()
        #######################

        # １文字ずつに変換
        char_list = list(conv.do(self.text))

        ####### 変換をset　　#######
        kakasi_.setMode('H', 'a')  # H(Hiragana) to a(roman)
        conv = kakasi_.getConverter()
        #######################

        for i in range(len(char_list)):
            self.lastText.append(conv.do(char_list[i]))

        return self.lastText
