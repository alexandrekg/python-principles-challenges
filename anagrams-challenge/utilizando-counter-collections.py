# criar a funcao
from collections import Counter


def is_anagram(word1: str, word2: str) -> bool:
    word1_count = word_count(word1)
    word2_count = word_count(word2)
    rules = [
        len(word1) == len(word2),
        word1_count == word2_count
    ]

    return all(rules)


def word_count(word: str) -> dict:
    return dict(Counter(word))


# criar testes baseado nos exemplos
print(is_anagram("typhoon", "opython"), is_anagram("typhoon", "opython") is True)
print(is_anagram("Alice", "Bob"), is_anagram("Alice", "Bob") is False)


# descobrir o que é um anagrama


