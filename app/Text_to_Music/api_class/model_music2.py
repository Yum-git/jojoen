class musicalConverter(object):

    def __init__(self, lastText):
        self.lastText = lastText
        self.musicalScore = []
        
    def convertMusic(self):
        vowel = []
        # ローマ字の末尾を取得
        for i in range(len(self.lastText)):
            vowel.append(self.lastText[i][-1])

        # 音階に変換
        for i in range(len(lastText)):
            if vowel[i] == "u":
                self.musicalScore.append("ド")
            elif vowel[i] == "e":
                self.musicalScore.append("レ")
            elif vowel[i] == "i":
                self.musicalScore.append("ミ")
            elif vowel[i] == "a":
                self.musicalScore.append("ファ")
            elif vowel[i] == "o":
                self.musicalScore.append("ソ")
            elif vowel[i].isalpha():
                self.musicalScore.append("ラ")
            else:
                self.musicalScore.append("シ")

        self.musicalScore.append("#ド")

        return self.musicalScore