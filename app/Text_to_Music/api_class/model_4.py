from tqdm import tqdm
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image

# 単語をもとに図を生成する
# ワードクラウド
class WordChange(object):
    def __init__(self, wordlist):
        self.wordlist = wordlist
    
    def Picture_create(self):
        wordcloud = WordCloud(
            font_path="./HGRGM.TTC",
            regexp="[\w']+",
            background_color='white',
            colormap='jet',
            width=800,
            height=800)
        
        wordcloud.fit_words(self.wordlist)

        wordcloud.to_file('../tmp/word.png')

        return '../tmp/word.png'

                            