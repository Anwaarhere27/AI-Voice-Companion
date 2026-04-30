import torch

# =========================
# AUDIO
# =========================
SAMPLE_RATE = 16000
CHANNELS = 1
CHUNK_DURATION = 5  # seconds

# =========================
# WHISPER
# =========================
WHISPER_MODEL_SIZE = "base"

# =========================
# GROQ
# =========================
GROQ_MODEL = "llama-3.1-8b-instant"
# =========================
# DEVICE
# =========================
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# =========================
# BARK
# =========================
BARK_SPEAKER = "v2/en_speaker_6"