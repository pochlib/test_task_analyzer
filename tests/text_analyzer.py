import pytest
from handlers.text_analyzer import analyze_text


def test_analyze_text_stop_words():
    text = "A is in on at to b"
    result = analyze_text(text)
    assert result["word_count"] == 7
    assert result["top_words"] == [
        {'count': 1, 'word': 'b'}, # b is not presented in stop words
    ]

def test_analyze_with_apostrophe():
    text = "I don't know if she's here."
    result = analyze_text(text)
    assert result["word_count"] == 6

def test_analyze_text_with_ellipsis():
    text = "I'm not sure about it... Wait"
    result = analyze_text(text)
    assert result["word_count"] == 6
    assert result["sentence_count"] == 2

def test_analyze_text_without_delimiters_one_word():
    text = "Wait \n"
    result = analyze_text(text)
    assert result["word_count"] == 1
    assert result["sentence_count"] == 1
    assert result["top_words"] == [
        {'count': 1, 'word': 'wait'}]

def test_analyze_text_with_quotes():
    text = "What does 'generics' mean? Generics are abstractions"
    result = analyze_text(text)

    assert result["word_count"] == 7
    assert result["sentence_count"] == 2
    assert result["top_words"] == [
        {'count': 2, 'word': 'generics'},  # without apostrophes + combined by lowercase
        {'count': 1, 'word': 'what'},
        {'count': 1, 'word': 'does'},
        {'count': 1, 'word': 'mean'},
        {'count': 1, 'word': 'abstractions'},
    ]

def test_analyze_text_numbers():
    text = "In 2023, the team processed 32 requests. Over the past 5 days, the system ran 32 tests."
    result = analyze_text(text)
    assert result["word_count"] == 17  # including numbers
    assert result["char_count_with_spaces"] == 87
    assert result["char_count_without_spaces"] == 71
    assert result["sentence_count"] == 2
    assert result["top_words"] == [
        {'count': 2, 'word': '32'},
        {'count': 1, 'word': '2023'},
        {'count': 1, 'word': 'team'},
        {'count': 1, 'word': 'processed'},
        {'count': 1, 'word': 'requests'}
   ]

def test_analyze_text_small_text():
    text = "Some example text. Another sentence!"
    result = analyze_text(text)

    assert result["word_count"] == 5
    assert result["char_count_with_spaces"] == 36
    assert result["char_count_without_spaces"] == 32
    assert result["sentence_count"] == 2
    assert result["top_words"] == [
        {"word": "some", "count": 1},
        {"word": "example", "count": 1},
        {"word": "text", "count": 1},
        {"word": "another", "count": 1},
        {"word": "sentence", "count": 1},
    ]


def test_analyze_text_medium_text():
    with open("./medium_text.txt", "r") as f:
        text = f.read()

    result = analyze_text(text)

    assert result["word_count"] == 64
    assert result["char_count_with_spaces"] == 365
    assert result["char_count_without_spaces"] == 300
    assert result["sentence_count"] == 9
    assert result["top_words"] == [
    { "word": "fox", "count": 6 },
    { "word": "dog", "count": 6 },
    { "word": "friendship", "count": 2 },
    { "word": "animals", "count": 2 },
    { "word": "over", "count": 1 }
  ]
