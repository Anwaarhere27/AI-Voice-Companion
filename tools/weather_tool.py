import re

def extract_weather_location(text: str):

    text = text.lower()

    # remove punctuation completely
    text = re.sub(r"[^\w\s]", "", text)

    if "weather" not in text:
        return None

    # extract after "in"
    if " in " in text:
        location = text.split(" in ")[-1].strip()
    else:
        location = text.replace("weather", "").strip()

    return clean_location(location)


def clean_location(location: str):

    if not location:
        return None

    location = location.lower()

    # remove noise words
    stop_words = [
        "today", "now", "please", "tell", "me"
    ]

    for word in stop_words:
        location = location.replace(word, "")

    location = location.strip()

    # 🧠 FINAL FIX: capitalize properly for API
    return location.title()