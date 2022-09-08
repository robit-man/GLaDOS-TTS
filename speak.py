import numpy as np
# pip3 install librosa==0.6.*, latest does not work
import librosa
import wave
from pydub import AudioSegment
from gtts import gTTS
from playsound import playsound
from main import start
import wavfile

def pitch_shift(sound, n_steps):
    y = np.frombuffer(sound._data, dtype=np.int16).astype(np.float32)/2**15
    y = librosa.effects.pitch_shift(y, sound.frame_rate, n_steps=n_steps)
    a  = AudioSegment(np.array(y * (1<<15), dtype=np.int16).tobytes(), frame_rate = sound.frame_rate, sample_width=2, channels = 1)
    return a

def speak(answer):
    tts = gTTS(answer, lang='en', tld='com')
    tts2 = gTTS(answer, lang='en', tld='ca')
    tts.save('answer.mp3')
    tts2.save('answer2.mp3')

    sound = AudioSegment.from_mp3("answer.mp3")
    soundb = AudioSegment.from_mp3("answer2.mp3")
    sound = pitch_shift(sound, 0)
    sound.export("answer.mp3")
    soundb = pitch_shift(soundb, -0.3)
    soundb.export("answer2.mp3")
    
    sound1 = AudioSegment.from_file("answer.mp3", format="mp3")
    sound2 = AudioSegment.from_file("answer2.mp3", format="mp3")

    # sound1 6 dB louder
    louder = sound1 + 4
    louder1 = sound2 + 6
    louder2 = sound1 + 4


    # sound1, with sound2 appended (use louder instead of sound1 to append the louder version)
    overlay = louder.overlay(louder2, position=0)
    overlay2 = overlay.overlay(louder1, position=0)

    # simple export
    file_handle = overlay2.export("answer1.wav", format="wav")
    #y, sr = librosa.load('answer.mp3')

    start('answer1.wav','answer1.wav',7)
    #augmented = augaudio.augment(y, 1, 4)

    #soundfile.write('answer.mp3', augmented, sr)
    playsound('answer1.wav')

    #engine.say(answer)
    #engine.runAndWait()   
