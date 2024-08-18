def div_3(num):
    return num % 3 == 0


print(div_3(6), div_3(6) is True)
print(div_3(9), div_3(9) is True)
print(div_3(5), div_3(5) is False)
print(div_3(27), div_3(27) is True)
print(div_3(25), div_3(25) is False)
print(div_3(30), div_3(30) is True)

