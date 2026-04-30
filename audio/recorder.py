import sounddevice as sd
import numpy as np
from config import SAMPLE_RATE, CHANNELS, CHUNK_DURATION


def record_audio():
    print("🎤 Listening...")

    audio = sd.rec(
        int(CHUNK_DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="float32"
    )

    sd.wait()

    return np.squeeze(audio)