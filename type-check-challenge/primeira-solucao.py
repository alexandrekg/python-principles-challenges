def only_ints(num1, num2):
    if type(num1) == int and type(num2) == int:
        return True
    return False

print(only_ints(1, 1), only_ints(1, 1) is True)
print(only_ints(1.2, 1), only_ints(1.2, 1) is False)
print(only_ints(5, 2), only_ints(5, 2) is True)

