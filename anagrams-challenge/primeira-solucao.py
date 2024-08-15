# criar a funcao
def is_anagram(word1: str, word2: str):
    word1_count = {}
    word2_count = {}
    for _c in word1:
        if _c in word1_count:
            word1_count[_c] += 1
        else:
            word1_count[_c] = 0

    for _c in word2:
        if _c in word2_count:
            word2_count[_c] += 1
        else:
            word2_count[_c] = 0

    rules = [
        len(word1) == len(word2),
        word1_count == word2_count
    ]

    return all(rules)



# criar testes baseado nos exemplos
print(is_anagram("typhoon", "opython"), is_anagram("typhoon", "opython") is True)
print(is_anagram("Alice", "Bob"), is_anagram("Alice", "Bob") is False)


# descobrir o que é um anagrama


