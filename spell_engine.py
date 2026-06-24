from spellchecker import SpellChecker

spell = SpellChecker()


def correct_text(text, technical_words):

    words = text.split()

    corrected_words = []

    misspelled = 0

    for word in words:

        clean_word = word.lower().strip(".,!?")

        if clean_word in technical_words:
            corrected_words.append(word)
            continue

        if clean_word not in spell:

            misspelled += 1

            correction = spell.correction(
                clean_word
            )

            if correction:
                corrected_words.append(
                    correction
                )
            else:
                corrected_words.append(
                    word
                )

        else:

            corrected_words.append(
                word
            )

    corrected_text = " ".join(
        corrected_words
    )

    return corrected_text, misspelled