import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

from audio.recorder import record_audio
from utils.helpers import save_audio

from stt.whisper_engine import transcribe

from llm.groq_client import ask_groq

from tts.edge_tts_engine import generate_speech
from audio.player import play_audio

# TOOLS
from tools.tool_router import detect_tool

from tools.weather_tool import extract_weather_location
from tools.weather_service import get_weather

from tools.calculator_tool import calculate

from tools.wikipedia_tool import search_wikipedia


# =========================
# EXIT DETECTION
# =========================
def should_exit(text: str):

    text = text.lower()

    exit_words = [
        "exit",
        "quit",
        "bye",
        "goodbye",
        "stop"
    ]

    return any(word in text for word in exit_words)


# =========================
# MAIN
# =========================
def main():

    print("\n==============================")
    print(" REALTIME AI AGENT ")
    print("==============================\n")

    while True:

        # =========================
        # RECORD AUDIO
        # =========================
        print("\n🎤 Listening...")

        audio_data = record_audio()

        save_audio(audio_data)

        # =========================
        # SPEECH TO TEXT
        # =========================
        user_text = transcribe("temp.wav")

        print(f"\n🧑 You: {user_text}")

        if not user_text:
            continue

        # =========================
        # EXIT
        # =========================
        if should_exit(user_text):

            goodbye = "Goodbye! Have a great day."

            print(f"\n🤖 AI: {goodbye}")

            audio_file = generate_speech(goodbye)

            play_audio(audio_file)

            break

        # =========================
        # TOOL DETECTION
        # =========================
        tool = detect_tool(user_text)

        print(f"\n🛠 Selected Tool: {tool}")

        # =========================
        # WEATHER TOOL
        # =========================
        if tool == "weather":

            location = extract_weather_location(user_text)

            ai_response = get_weather(location)

        # =========================
        # CALCULATOR TOOL
        # =========================
        elif tool == "calculator":

            expression = (
                user_text
                .replace("calculate", "")
                .replace("what is", "")
                .strip()
            )

            ai_response = calculate(expression)

        # =========================
        # WIKIPEDIA TOOL
        # =========================
        elif tool == "wikipedia":

            query = user_text.lower()

            wiki_phrases = [
                "who is",
                "what is",
                "tell me about",
                "information about",
            ]

            for phrase in wiki_phrases:
                query = query.replace(phrase, "")

            query = query.strip()

            ai_response = search_wikipedia(query)

        # =========================
        # NORMAL CHAT
        # =========================
        else:

            ai_response = ask_groq(user_text)

        # =========================
        # PRINT RESPONSE
        # =========================
        print(f"\n🤖 AI: {ai_response}")

        # =========================
        # TTS
        # =========================
        audio_file = generate_speech(ai_response)

        play_audio(audio_file)


if __name__ == "__main__":
    main()