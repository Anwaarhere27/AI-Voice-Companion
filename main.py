import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

from audio.recorder import record_audio
from utils.helpers import save_audio
from stt.whisper_engine import transcribe
from llm.groq_client import ask_groq

from tts.edge_tts_engine import generate_speech
from audio.player import play_audio


def main():

    print("\n==============================")
    print(" REALTIME AI VOICE COMPANION ")
    print("==============================\n")

    while True:

        # ======================
        # RECORD AUDIO
        # ======================
        print("\n🎤 Listening...")
        audio_data = record_audio()

        save_audio(audio_data)

        # ======================
        # SPEECH TO TEXT
        # ======================
        user_text = transcribe("temp.wav")

        print(f"\n🧑 You: {user_text}")

        if not user_text or user_text.strip() == "":
            continue

        # Exit command
        if "exit" in user_text.lower():
            print("👋 Goodbye!")
            break

        # ======================
        # LLM RESPONSE (GROQ)
        # ======================
        ai_response = ask_groq(user_text)

        print(f"\n🤖 AI: {ai_response}")

        # ======================
        # TEXT TO SPEECH (FAST)
        # ======================
        audio_file = generate_speech(ai_response)

        # ======================
        # PLAY AUDIO
        # ======================
        play_audio(audio_file)


if __name__ == "__main__":
    main()