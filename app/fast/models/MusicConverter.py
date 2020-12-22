import random

tmp_light_music_list = []
tmp_dark_music_list = []

with open("/var/www/fast/static/text/music_list_posi.txt", "r") as f:
    for tmp_light_music in [s.strip() for s in f.readlines()]:
        tmp_light_music_list.append(list(tmp_light_music.split()))

with open("/var/www/fast/static/text/music_list_nega.txt", "r") as f:
    for tmp_dark_music in [s.strip() for s in f.readlines()]:
        tmp_dark_music_list.append(list(tmp_dark_music.split()))


# ローマ字を音楽（♪）に変換する
class musicalConverter(object):
    def __init__(self, posinega_score):
        self.musicalScore = []  # type: list
        self.posinega_score = posinega_score  # type: int

    def convertMusic(self):
        if self.posinega_score >= 0:
            rand = random.randrange(10)
            for rand_search in range(10):
                if rand_search == rand:
                    self.musicalScore = tmp_light_music_list[rand_search]
                    break

        elif self.posinega_score < 0:
            rand = random.randrange(7)
            for rand_search in range(7):
                if rand_search == rand:
                    self.musicalScore = tmp_dark_music_list[rand_search]
                    break

        return self.musicalScore
