
def double_letters(word):
    counter = 0

    for char_ in word:
        if len(word) > counter + 1:
            if char_ == word[counter + 1]:
                return True
        counter += 1
    return False


print(double_letters('hello'), double_letters('hello') is True)
print(double_letters('word'), double_letters('word') is False)
print(double_letters('javinescula'), double_letters('javinescula') is False)
print(double_letters('margarina'), double_letters('margarina') is False)
print(double_letters('cacetinho'), double_letters('cacetinho') is False)
print(double_letters('café'), double_letters('café') is False)
print(double_letters('happy'), double_letters('happy') is True)
