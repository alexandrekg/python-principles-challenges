

def capital_indexes(word):
    indexes = []
    index_counter = 0
    for character in word:
        if character.isupper():
            print(index_counter)
            indexes.append(index_counter)
        index_counter += 1
    return indexes


print(f"Deve retornar 0, 2, 4 | {capital_indexes('HeLlO') == [0, 2, 4]}")
print(f"Deve retornar 0, 1, 3 | {capital_indexes('TEsT') == [0, 1, 3]}")
