import torch
import numpy as np
from transformers import AutoProcessor, BarkModel

from config import BARK_SPEAKER, DEVICE

print("Loading Bark model...")

processor = AutoProcessor.from_pretrained("suno/bark")

model = BarkModel.from_pretrained(
    "suno/bark",
    torch_dtype=torch.float32,
    use_safetensors=False
).to(DEVICE)

model.eval()


def generate_speech(text):

    print("🎙 Generating speech...")

    inputs = processor(
        text=text,
        voice_preset=BARK_SPEAKER,
        return_tensors="pt"
    )

    inputs = {k: v.to(DEVICE) for k, v in inputs.items()}

    with torch.no_grad():
        audio = model.generate(**inputs)

    print("✅ Bark generation finished")

    audio = audio.cpu().numpy().squeeze()

    print("🔍 Raw audio shape:", audio.shape)
    print("🔍 Max value:", np.max(audio))

    # Safety cleanup
    audio = np.nan_to_num(audio)
    audio = audio.astype(np.float32)

    max_val = np.max(np.abs(audio))
    if max_val > 0:
        audio = audio / max_val

    sample_rate = model.generation_config.sample_rate

    return audio, sample_rate