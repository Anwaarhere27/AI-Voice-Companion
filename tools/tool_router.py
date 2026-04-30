import re


def contains_math(text):

    math_patterns = [
        r"\d+\s*\+\s*\d+",
        r"\d+\s*-\s*\d+",
        r"\d+\s*\*\s*\d+",
        r"\d+\s*/\s*\d+",
        r"\d+\s+plus\s+\d+",
        r"\d+\s+minus\s+\d+",
        r"\d+\s+times\s+\d+",
        r"\d+\s+multiplied by\s+\d+",
        r"\d+\s+divided by\s+\d+",
    ]

    return any(re.search(pattern, text) for pattern in math_patterns)


def detect_tool(user_text: str):

    text = user_text.lower()

    # =========================
    # WEATHER
    # =========================
    if "weather" in text:
        return "weather"

    # =========================
    # CALCULATOR
    # =========================
    if contains_math(text):
        return "calculator"

    calc_keywords = [
        "calculate",
        "math",
        "solve",
    ]

    if any(word in text for word in calc_keywords):
        return "calculator"

    # =========================
    # WIKIPEDIA
    # =========================
    wiki_keywords = [
        "who is",
        "tell me about",
        "wikipedia",
        "information about",
    ]

    if any(word in text for word in wiki_keywords):
        return "wikipedia"

    # =========================
    # DEFAULT CHAT
    # =========================
    return "chat"