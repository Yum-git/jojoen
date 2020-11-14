from django.test import TestCase


# Create your tests here.
# まとめフォルダ
from .api_class import models_bunde
from rest_framework import status

class QuestionModel(TestCase):
    def test_pattern_1_no_sentence(self):
        sentence = ""
        Response = models_bunde.StartClass(sentence)

        self.assertEqual(Response.main_(), ('None', 'None', 204))

    def test_pattern_2_basic_sentence_1(self):
        sentence = "珍野家で飼われている雄猫。本編の語り手。「吾輩」は一人称であり、彼自身に名前はない。人間の生態を鋭く観察したり、猫ながら古今東西の文芸に通じており哲学的な思索にふけったりする。人間の内心を読むこともできる。三毛子に恋心を抱いている。最後は飲み残しのビールに酔い、水甕に落ちて出られぬまま溺れ死ぬ（第十一話）。"
        Response = models_bunde.StartClass(sentence)

        self.assertNotEqual(Response.main_(), ('None', 'None', 204))

    def test_pattern_3_basic_sentence_2(self):
        sentence = "物は性を有し、性は物を具す。性は物と混成して罅縫無し。故に、其の一や全なり。性は体に偶し、物は気に偶す。物は性と粲立して条理あり。故に、其の二や偏なり。性は物に性し、物は性に物す。故に、一即一一、一一即一なり。気は天を成し、物は地を成す。性は一を具し、体は一を欠す。具一欠二、剖して経を為し、一気一物、対して緯を為す。"
        Response = models_bunde.StartClass(sentence)

        self.assertNotEqual(Response.main_(), ('None', 'None', 204))

