
def capital_indexes(word):
    return [word.index(character) for character in word if character.isupper()]


print(f"Deve retornar 0, 2, 4 | {capital_indexes('HeLlO') == [0, 2, 4]}")
print(f"Deve retornar 0, 1, 3 | {capital_indexes('TEsT') == [0, 1, 3]}")

