import random
tmp_light_rhythm1 = [1/4, 1/8, 1/8, 1/8, 1/4, 1/8, 1/4, 1/8, 1/8, 1/4, 1/4]
tmp_light_rhythm2 = [1/8, 1/4, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/4, 1/8, 1/4, 1/4]
tmp_light_rhythm3 = [3/16, 1/16, 3/16, 1/16, 3/16, 1/16, 3/16, 1/16, 3/16, 1/16, 3/16, 1/16, 1/16]
tmp_light_rhythm4 = [1/8, 1/4, 1/8, 1/8, 1/8, 1/4, 1/4, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8]
tmp_light_rhythm5 = [1/8, 1/8, 1/8, 1/8, 1/4, 1/4]

tmp_dark_rhythm1 = [1/8, 1/8, 1/4, 1/4, 1/4, 1/4, 1/8, 1/8]
tmp_dark_rhythm2 = [1/4, 1/4, 1/4, 1/8, 1/8]
tmp_dark_rhythm3 = [1/4, 3/8, 1/8]
tmp_dark_rhythm4 = [3/8, 1/8, 1/4, 1/4]
tmp_dark_rhythm5 = [1/12, 1/12, 1/12, 1/12, 1/12, 1/12, 1/4, 1/4]
tmp_dark_rhythm6 = [1/2, 1/4, 3/16, 1/16]

class makeRhythm(object):

    def __init__(self, PosiNegaScore, musicalScore):
        self.PosiNegaScore = PosiNegaScore
        self.musicalScore = musicalScore
        self.rhythm = []
        self.melody = []
        
    def rhythmMake(self):
        while True:
            if self.PosiNegaScore >=0:
                rand = random.randrange(5)
                if rand == 0:
                    self.rhythm = self.rhythm + tmp_light_rhythm1
                elif rand == 1:
                    self.rhythm = self.rhythm + tmp_light_rhythm2
                elif rand == 2:
                    self.rhythm = self.rhythm + tmp_light_rhythm3
                elif rand == 3:
                    self.rhythm = self.rhythm + tmp_light_rhythm4
                elif rand == 4:
                    self.rhythm = self.rhythm + tmp_light_rhythm5

            elif self.PosiNegaScore < 0:
                rand = random.randrange(5)
                if rand == 0:
                    self.rhythm = self.rhythm + tmp_dark_rhythm1
                elif rand == 1:
                    self.rhythm = self.rhythm + tmp_dark_rhythm2
                elif rand == 2:
                    self.rhythm = self.rhythm + tmp_dark_rhythm3
                elif rand == 3:
                    self.rhythm = self.rhythm + tmp_dark_rhythm4
                elif rand == 4:
                    self.rhythm = self.rhythm + tmp_dark_rhythm5

            if len(self.rhythm) > len(self.musicalScore)+1:
                break
        return 

    def melodyMake(self):
        for i in range(len(self.musicalScore)):
            self.melody.append([self.musicalScore[i], self.rhythm[i]])
        return self.melody
