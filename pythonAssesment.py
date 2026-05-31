import re
from collections import Counter


def count_specific_word(text: str, word: str) -> int:
    words = re.findall(r'\b\w+\b', text.lower())
    return words.count(word.lower())


def identify_most_common_word(text: str) -> str | None:
    words = re.findall(r'\b\w+\b', text.lower())
    if not words:
        return None
    counter = Counter(words)
    return counter.most_common(1)[0][0]


def calculate_average_word_length(text: str) -> float:
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return 0
    lengths = [len(word) for word in words]
    return sum(lengths) / len(words)


def count_paragraphs(text: str) -> int:
    if not text.strip():
        return 1
    paragraphs = [p for p in text.split("\n\n") if p.strip()]
    return len(paragraphs)


def count_sentences(text: str) -> int:
    if not text.strip():
        return 1
    sentences = re.split(r'[.!?]+', text.strip())
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)



sample_text = """
Python is great. Python is powerful!
It is used in web development, data science, and AI.

This is another paragraph. It has two sentences.
"""

print("Count 'Python':", count_specific_word(sample_text, "Python"))
print("Most common word:", identify_most_common_word(sample_text))
print("Average word length:", calculate_average_word_length(sample_text))
print("Paragraph count:", count_paragraphs(sample_text))
print("Sentence count:", count_sentences(sample_text))