from faster_whisper import WhisperModel
from config import WHISPER_MODEL_SIZE, DEVICE

print("Loading Whisper model...")

model = WhisperModel(
    WHISPER_MODEL_SIZE,
    device=DEVICE,
    compute_type="float16" if DEVICE == "cuda" else "int8"
)


def transcribe(audio_path):

    segments, info = model.transcribe(audio_path)

    text = ""

    for segment in segments:
        text += segment.text + " "

    return text.strip()