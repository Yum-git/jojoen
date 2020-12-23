import oseti


# ポジティブ度を測定する
class PosiNega(object):
    def __init__(self, text: str):
        self.text = text  # type: str
        self.posinega_score = 0  # type: int
        self.tangoNum = 0  # type: int

    def posi_nega_jud(self):
        analyzer = oseti.Analyzer()  # type: Analyzer
        posinega_text_list = analyzer.count_polarity(self.text)  # type: list

        for i in range(len(posinega_text_list)):
            if posinega_text_list[i]['positive'] > 0:
                self.posinega_score += posinega_text_list[i]['positive']
            if posinega_text_list[i]['negative'] > 0:
                self.posinega_score -= posinega_text_list[i]['negative']

        self.tangoNum = len(posinega_text_list)

        return self.posinega_score, self.tangoNum
