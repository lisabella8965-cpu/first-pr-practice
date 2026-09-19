def count_words(text):
    """Return the number of whitespace-separated words in text."""
    return len(text.split())


def longest_word(text):
    """Return the longest word in text (first one, on ties)."""
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)


if __name__ == "__main__":
    sample = "This is a small example sentence for word stats"
    print(f"word count: {count_words(sample)}")
    print(f"longest word: {longest_word(sample)}")
