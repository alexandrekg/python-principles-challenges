def list_xor(n, list1, list2):
    return (n in list1) ^ (n in list2)


print(list_xor(1, [1, 2, 3], [4, 5, 6]) == True)
print(list_xor(1, [1, 2, 3], [1, 5, 6]) == False)
print(list_xor(1, [0, 0, 0], [4, 5, 6]) == False)
print(list_xor(1, [0, 2, 3], [1, 5, 6]) == True)


