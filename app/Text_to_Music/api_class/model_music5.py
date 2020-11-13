import oseti

class PosiNega(object):

    def __init__(self, text):
        self.text = text
        self.PosiNegaScore = 0
        self.tangoNum = 0

    def posiNegaJud(self):
        analyzer = oseti.Analyzer()
        kekka = analyzer.count_polarity(self.text)

        for i in range(len(kekka)):
            if kekka[i]['positive'] > 0:
                self.PosiNegaScore += kekka[i]['positive']
            if kekka[i]['negative'] > 0:
                self.PosiNegaScore -= kekka[i]['negative']

        self.tangoNum = len(kekka)

        return self.PosiNegaScore, self.tangoNum
