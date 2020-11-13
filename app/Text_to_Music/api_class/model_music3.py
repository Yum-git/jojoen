class makeRhythm(object):

    def __init__(self, PosiNegaScore, musicalScore):
        self.PosiNegaScore = PosiNegaScore
        self.musicalScore = musicalScore
        self.rhythm = []
        self.melody = []
        
    def rhythm(self):
        tmp_rhythm1 = [1/2, 1/2]
        tmp_rhythm2 = [1/4, 1/4, 1/4, 1/4]
        tmp_rhythm3 = [1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8]
        tmp_rhythm4 = [1/16, 1/16, 1/16, 1/16, 1/16, 1/16, 1/16, 1/16, 1/16, 1/16, 1/16, 1/16, 1/16, 1/16, 1/16, 1/16]


        while True:
        rand = random.randrange(4)
        if rand == 1:
            self.rhythm = self.rhythm + tmp_rhythm1
        elif rand == 2:
            self.rhythm = self.rhythm + tmp_rhythm2
        elif rand == 3:
            self.rhythm = self.rhythm + tmp_rhythm3
        elif rand == 4:
            self.rhythm = self.rhythm + tmp_rhythm4
        if len(self.rhythm) > len(self.musicalScore)+1:
            break
        return 

    def melody(self):
        for i in range(len(self.musicalScore)):
            self.melody.append([ self.musicalScore[i], self.rhythm[i]])
        return self.melody
