from word_stats import count_words, longest_word


def test_count_words_basic():
    assert count_words("This is a small example") == 5


def test_count_words_empty_string():
    assert count_words("") == 0


def test_count_words_extra_whitespace():
    assert count_words("  lots   of   space   here  ") == 4


def test_longest_word_basic():
    assert longest_word("This is a small example sentence") == "sentence"


def test_longest_word_empty_string():
    assert longest_word("") == ""


def test_longest_word_first_on_tie():
    assert longest_word("cat dog fox") == "cat"
