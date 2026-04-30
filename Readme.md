# 🎙️ AI Voice Companion (Whisper + GROQ + TTS + Tools)

A real-time voice-based AI agent that listens to your speech, understands intent, routes it to the correct tool (LLM / calculator / Wikipedia / weather), and responds back using speech.

This project demonstrates a **multi-tool AI agent architecture** with speech-to-text, LLM reasoning, tool execution, and text-to-speech in a single pipeline.

---

# 🚀 Features

- 🎤 Real-time Speech-to-Text (Whisper)
- 🧠 LLM responses (GROQ API)
- 🌤 Live Weather Integration (OpenWeather API)
- ➗ Smart Calculator (natural language math)
- 📚 Wikipedia knowledge lookup
- 🔊 Text-to-Speech (Edge TTS / Bark support)
- 🧠 Tool routing (basic rule-based agent system)
- 📴 Exit commands: `bye`, `exit`, `quit`

---

### Create .env File
- Write the following line in the file:
- GROQ_API_KEY=YOUR GROQ API KEY
- WEATHER_API_KEY=YOUR WEATHER API KEY
- Add your GROQ API KEY
- ADD YOUR WEATHER API KEY FROM weatherapi.com

#### How To Run:
- Clone repo
- Run following commands in the terminal:
- python -m venv venv
- venv/scripts/activate
- pip install -r requirements.txt
- python main.py

---
