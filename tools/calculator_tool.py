import re
import numexpr as ne


def normalize_expression(expression: str):

    expression = expression.lower()

    # Convert words to math symbols
    replacements = {
        "plus": "+",
        "minus": "-",
        "times": "*",
        "multiplied by": "*",
        "x": "*",
        "into": "*",
        "divided by": "/",
    }

    for word, symbol in replacements.items():
        expression = expression.replace(word, symbol)

    # Remove natural language clutter
    remove_words = [
        "what is",
        "calculate",
        "how much is",
        "please",
        "can you tell me",
        "?",
        "=",
    ]

    for word in remove_words:
        expression = expression.replace(word, "")

    # 🚀 CRITICAL FIX: remove ALL whitespace properly
    expression = expression.strip()

    # remove extra spaces inside expression
    expression = re.sub(r"\s+", " ", expression)

    # remove invalid characters (safety)
    expression = re.sub(r"[^0-9+\-*/(). ]", "", expression)

    # final cleanup again
    expression = expression.strip()

    return expression


def calculate(expression: str):

    try:

        expression = normalize_expression(expression)

        print("🧮 CLEANED EXPRESSION:", repr(expression))

        result = ne.evaluate(expression)

        return f"The answer is {result.item()}"

    except Exception as e:

        print("CALCULATOR ERROR:", e)

        return "Sorry, I could not calculate that."