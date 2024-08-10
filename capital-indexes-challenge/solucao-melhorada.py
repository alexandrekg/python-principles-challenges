
def capital_indexes(word):
    return [word.index(character) for character in word if character.isupper()]


print(f"Deve retornar 0, 2, 4 | {capital_indexes('HeLlO') == [0, 2, 4]}")
