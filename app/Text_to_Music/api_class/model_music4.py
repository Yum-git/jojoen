import numpy as np
import wave
import struct
import random


### 各種定数
VOLUME = 1
SAMPLE_RATE = 44100
normal_TONES = {
    'ド': 261.626 ,
    'レ': 293.665 ,
    'ミ': 329.628 ,
    'ファ': 349.228 ,
    'ソ': 391.995 ,
    'ラ': 440.000 ,
    'シ': 493.883 ,
    '#ド': 277.183
}

# 長調
light_TONES = {
    'ド': 261.626 ,
    'レ': 293.665 ,
    'ミ': 329.628 ,
    'ファ': 349.228 ,
    'ソ': 391.995 ,
    'ラ': 440.000 ,
    'シ': 493.883 ,
    '#ド': 277.183	
}
# 単調
dark_TONES = {
    'ド': 261.626 ,
    'レ': 293.665 ,
    'ミ': 311.127 ,
    'ファ': 349.228 ,
    'ソ': 391.995 ,
    'ラ': 415.305	,
    'シ': 466.164 ,
    '#ド': 277.183	
}

#################### レコーダークラス ##############################
class Recorder:
    def __init__(self, PosiNegaScore, melody):
        # 楽譜格納
        self.melody = melody
        self.PosiNegaScore = PosiNegaScore

    def generate_tone(self, tones, beat, bpm=120):
        if self.PosiNegaScore >=0:
            TONES = light_TONES  
        elif self.PosiNegaScore < 0:
            TONES = dark_TONES  

        sec = bpm / 60 * beat
        t = np.arange(0, SAMPLE_RATE * sec)
        y = None
        for tone in tones:
            # 和音対応（各音の配列を足し合わせると和音になる）
            f = TONES[tone] if tone in TONES else 0
            if y is None:
                y = VOLUME * np.sin(2 * np.pi * f * t / SAMPLE_RATE)
            else:
                y += VOLUME * np.sin(2 * np.pi * f * t / SAMPLE_RATE).tolist()
        return y.tolist()

    def save_as_wave(self, y, filename):
        max_num = 32767.0 / max(y)
        bit = [int(x * max_num) for x in y]
        waves = struct.pack("h" * len(bit), *bit)
        w = wave.Wave_write(filename)
        w.setparams((1, 2, SAMPLE_RATE, len(waves), 'NONE', 'not compressed'))
        w.writeframes(waves)
        w.close()

    def save(self, filename):
        song = []
        for note in self.melody:
            song += self.generate_tone(*note)
        self.save_as_wave(np.array(song), filename)