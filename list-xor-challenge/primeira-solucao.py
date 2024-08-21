def list_xor(n, list1, list2):
    if n in list1 and n not in list2:
        return True
    elif n not in list1 and n in list2:
        return True

    return False

print(list_xor(1, [1, 2, 3], [4, 5, 6]) == True)
print(list_xor(1, [1, 2, 3], [1, 5, 6]) == False)
print(list_xor(1, [0, 0, 0], [4, 5, 6]) == False)
print(list_xor(1, [0, 2, 3], [1, 5, 6]) == True)


