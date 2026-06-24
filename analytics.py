import math
import re

def calculate_analytics(text):

    words = text.split()

    word_count = len(words)

    char_count = len(text)

    sentence_count = len(
        re.findall(r"[.!?]+", text)
    )

    if sentence_count == 0 and word_count > 0:
        sentence_count = 1

    reading_time = (
        math.ceil(word_count / 200)
        if word_count > 0 else 0
    )

    avg_length = (
        sum(len(word) for word in words)
        / word_count
        if word_count else 0
    )

    if avg_length < 5:
        vocabulary = "Beginner"

    elif avg_length < 8:
        vocabulary = "Intermediate"

    else:
        vocabulary = "Advanced"

    return {
        "words": word_count,
        "characters": char_count,
        "sentences": sentence_count,
        "reading_time": reading_time,
        "vocabulary": vocabulary
    }