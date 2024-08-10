

def capital_indexes(word):
    indexes = []
    for character in word:
        if character.isupper():
            indexes.append(word.index(character))
    return indexes


print(f"Deve retornar 0, 2, 4 | {capital_indexes('HeLlO') == [0, 2, 4]}")
