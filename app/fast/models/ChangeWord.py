from janome.tokenizer import Tokenizer


# 文章を単語に分ける（形態素解析）
class ChangeWord(object):
    def __init__(self, sentence):
        self.sentence = sentence
        self.words = {}
        self.tokens = None

    # 記号かどうかを判別する関数
    def find_kigou(self, string):
        for s in string:
            if s in ["!", "?", "[", "]", "(", ")", "「", "」", "！", "？", "（", "）", "'", '"', ",", "."]:
                return False
        return True

    # 一文字だけの言葉を削除関数
    def token(self, h):
        m = [chr(i) for i in range(12354, 12354 + 82)]
        for token in self.tokens:
            word = token.surface
            hinsi = token.part_of_speech.split(',')[0]
            if hinsi == h:
                key = word
                if key not in self.words:
                    if self.find_kigou(key):
                        # 一文字ひらがなの場合を削除
                        if len(key) == 1 and key not in m:
                            self.words[key] = 1
                        # 二文字ひらがなの場合を削除
                        if len(key) == 2 and (key[0] not in m and key[1] not in m):
                            self.words[key] = 1
                        # 三文字以上はすべて許可
                        if len(key) >= 3:
                            self.words[key] = 1
                else:
                    self.words[key] += 1
        return self.words

    # 形態素解析
    def Morphological(self):
        sentence_ = self.sentence
        sentence_ = sentence_.replace('\n', '')

        t = Tokenizer()
        tokens = t.tokenize(sentence_)

        self.tokens = tokens

    def main_(self, speech):
        self.Morphological()
        return self.token(speech)
