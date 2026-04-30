from scipy.io.wavfile import write
from config import SAMPLE_RATE


def save_audio(audio_data, filename="temp.wav"):
    write(filename, SAMPLE_RATE, audio_data)