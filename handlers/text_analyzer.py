STOP_WORDS = [
    "the",
    "a",
    "an",
    "is",
    "are",
    "was",
    "were",
    "in",
    "on",
    "at",
    "to",
    "and",
    "or",
    "but",
    "of",
    "for",
    "with",
    "not",
    "it",
    "this",
    "that",
]

DELIMITERS = [".", "!", "?"]
PUNCTUATION = [",", '"']

def get_top_five(words):
    top_five = {}

    for key, value in words.items():
        if key in STOP_WORDS:
            continue
        if len(top_five) < 5:
            top_five[key] = value
        else:
            smallest_value = min(top_five.values())
            smallest_key = [
                key for key, value in top_five.items() if value == smallest_value
            ][0]
            if value > smallest_value:
                del top_five[smallest_key]
                top_five[key] = value
    top_five = [{"word": key, "count": value} for key, value in top_five.items()]

    return sorted(top_five, key=lambda entry: entry["count"], reverse=True)

def analyze_text(text: str) -> dict:
    word_count = 0
    character_count_with_spaces = len(text)
    character_count_without_spaces = 0
    sentence_count = 0
    words = {}

    word = ""

    for char in text:
        if not char.isspace():
            character_count_without_spaces += 1

        if char.isalnum() or char == "'":
            word += char.lower()
        else:
            if word and char not in PUNCTUATION:
                word_count += 1
                word = word.strip("'")
                words[word] = words.get(word, 0) + 1
                if word and char in DELIMITERS:
                    sentence_count += 1
                word = ""

            if word and char in DELIMITERS:
                sentence_count += 1

    if word:
        word_count += 1
        sentence_count += 1
        words[word] = words.get(word, 0) + 1

    if words and not sentence_count:
        sentence_count += 1
    top_words = get_top_five(words)

    return {
        "word_count": word_count,
        "char_count_with_spaces": character_count_with_spaces,
        "char_count_without_spaces": character_count_without_spaces,
        "sentence_count": sentence_count,
        "top_words": top_words,
    }

print(analyze_text(text = 'What'))

