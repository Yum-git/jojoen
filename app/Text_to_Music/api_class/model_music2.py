import random

tmp_light_music1 = ["ド","#ド","シ","ソ","ミ","ラ","ファ","レ","ソ","ミ","ド","レ","ミ","ファ","シ","ド","レ","ミ","ファ","ソ"]
tmp_light_music2 = ["シ","ソ","ミ","ファ","ソ","ド","ラ","ファ","#ド","シ","ラ","ソ","#ド","ソ","ファ","ラ","ド","シ","ソ","レ","ソ"]
tmp_light_music3 = ["ド","#ド","ミ","レ","ソ","ソ","ファ","ファ","ラ","ラ","ド","#ド","シ","シ","ソ","ソ","レ","レ","ミ","ミ"]
tmp_light_music4 = ["ミ","ソ","ミ","ド","ファ","ラ","ファ","ド","ミ","ソ","ミ","#ド","シ","ソ","ファ","レ"]
tmp_light_music5 = ["ミ","ソ","#ド","シ","ラ","ファ","レ","ソ","ド","ミ","ファ","レ","ソ","シ","レ","ソ"]
tmp_light_music6 = ["ド","ミ","ソ","#ド","ソ","ミ","ファ","ラ","#ド","ファ","ド","ラ","ソ","シ","レ","ソ","レ","シ","ド","ソ","ド","ミ","ド","ソ"]
tmp_light_music7 = ["ソ","シ","ラ","レ","ソ","ラ","シ","ソ","シ","ソ","ラ","レ","レ","ラ","シ","ソ"]
tmp_light_music8 = ["ミ","#ド","シ","ラ","ソ","ミ","レ","ド","シ","レ","ソ","シ","ド","ミ","ド","ソ","ド","ミ","ファ","ソ","ラ","レ","ミ","ファ","ソ","シ","レ","ド","ミ","ソ","ド"]
tmp_light_music9 = ["ソ","ミ","ド","ラ","ファ","ミ","レ","ソ","ファ","ミ","ソ","ミ","ド","ラ","ファ","ミ","レ","ソ","ミ","#ド"]
tmp_light_music10 = ["ソ","シ","ソ","レ","シ","レ","ソ","シ","ラ","#ド","ラ","ファ","レ", "ファ","ラ","ド","シ","レ","シ","ソ","レ","ソ","レ","ソ","シ","レ","ド","レ","ド","ラ","ファ","ラ","ファ","レ"]

tmp_dark_music1 = ["シ","ド","レ","シ","ラ","ファ","ラ","シ","ラ","ファ","ラ","ド","ラ","ファ","レ","ド","レ"]
tmp_dark_music2 = ["シ","ド","ファ","ラ","ソ","ファ","ミ","レ","ド","ファ","シ","ド","ファ","ミ","レ","ド","レ"]
tmp_dark_music3 = ["ミ","ラ","シ","レ","ド","シ","ラ","ド","レ","ラ","ミ","ド","ファ","ソ","ミ","ファ","シ"]
tmp_dark_music4 = ["ソ","シ","ミ","ソ","ファ","ミ","レ","ミ","レ","ド","シ","レ","ド","ラ","ソ","ラ"]
tmp_dark_music5 = ["ファ","ミ","レ","ファ","ラ","シ","レ","ド","シ","レ","ファ","ラ","ド","シ","ラ","ソ","ファ","ラ","ソ"]
tmp_dark_music6 = ["レ","ソ","レ","ソ","ド","ソ","ラ","ソ","ソ","ファ","ソ","レ","ファ","レ","ソ","シ","ド","レ","レ","ソ"]
tmp_dark_music7 = ["ミ","ラ","シ","ド","シ","ラ","ミ","ミ","ラ","シ","#ド","ソ","ラ","ファ","レ","#ド","シ","ド","シ","ラ","ミ"]

class musicalConverter(object):

    def __init__(self, PosiNegaScore):
        self.musicalScore = []
        
    def convertMusic(self):
        if PosiNegaScore >= 0:
            rand = random.randrange(10)
        if rand == 0:
            self.musicalScore = tmp_light_music1
        elif rand == 1:
            self.musicalScore = tmp_light_music2
        elif rand == 2:
            self.musicalScore = tmp_light_music3
        elif rand == 3:
            self.musicalScore = tmp_light_music4
        elif rand == 4:
            self.musicalScore = tmp_light_music5
        elif rand == 5:
            self.musicalScore = tmp_light_music6
        elif rand == 6:
            self.musicalScore = tmp_light_music7
        elif rand == 7:
            self.musicalScore = tmp_light_music8
        elif rand == 8:
            self.musicalScore = tmp_light_music9
        elif rand == 9:
            self.musicalScore = tmp_light_music10

        elif PosiNegaScore < 0:
        rand = random.randrange(7) 
        if rand == 0:
            self.musicalScore = tmp_dark_music1
        elif rand == 1:
            self.musicalScore = tmp_dark_music2
        elif rand == 2:
            self.musicalScore = tmp_dark_music3
        elif rand == 3:
            self.musicalScore = tmp_dark_music4
        elif rand == 4:
            self.musicalScore = tmp_dark_music5
        elif rand == 5:
            musicalScore = tmp_dark_music6
        elif rand == 6:
            musicalScore = tmp_dark_music7

        return self.musicalScore