from playsound import playsound
import os


def play_audio(file_path):

    print("🔊 Playing audio...")

    try:
        playsound(file_path)

        print("✅ Done")

        # SAFE CLEANUP (important for Windows lock issues)
        os.remove(file_path)

    except Exception as e:
        print("❌ Playback error:", e)