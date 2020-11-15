from tqdm import tqdm
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image


# 単語をもとに図を生成する
# ワードクラウド
class WordChange(object):
    def __init__(self, wordlist, posi_score):
        self.wordlist = wordlist
        self.posi_score = posi_score

    def Picture_create(self):
        # if self.posi_score > 0:
        #     font_path = "./uzura.ttf"
        # else:
        #     font_path = "./Makinas.ttf"

        font_path = "/var/www/flaskr/models/ipaexg.ttf"

        wordcloud = WordCloud(
            # フォント変えてどうにか
            font_path=font_path,
            regexp="[\w']+",
            background_color='white',
            colormap='jet',
            width=800,
            height=800)

        try:
            wordcloud.fit_words(self.wordlist)
        except ValueError:
            return False
        wordcloud.to_file('../tmp/word.png')

        return '../tmp/word.png'
                            