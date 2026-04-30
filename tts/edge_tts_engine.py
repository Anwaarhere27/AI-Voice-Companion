import asyncio
import edge_tts
import time
import os

VOICE = "en-US-AriaNeural"


async def _speak(text, output_file):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(output_file)


def generate_speech(text):

    print("🎙 Generating speech (FAST MODE)...")

    # UNIQUE FILE NAME (IMPORTANT FIX)
    filename = f"response_{int(time.time() * 1000)}.mp3"

    asyncio.run(_speak(text, filename))

    return filename