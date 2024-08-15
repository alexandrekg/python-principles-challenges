# criar a funcao
def is_anagram(word1: str, word2: str):
    word1_count = word_count(word1)
    word2_count = word_count(word2)
    rules = [
        len(word1) == len(word2),
        word1_count == word2_count
    ]

    return all(rules)


def word_count(word):
    _word_count = {}
    for _c in word:
        if _c in _word_count:
            _word_count[_c] += 1
        else:
            _word_count[_c] = 0
    return _word_count


# criar testes baseado nos exemplos
print(is_anagram("typhoon", "opython"), is_anagram("typhoon", "opython") is True)
print(is_anagram("Alice", "Bob"), is_anagram("Alice", "Bob") is False)


# descobrir o que é um anagrama


