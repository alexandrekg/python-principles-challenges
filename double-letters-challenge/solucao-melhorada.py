
def double_letters(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return True
        
    return False


print(double_letters('hello'), double_letters('hello') is True)
print(double_letters('word'), double_letters('word') is False)
print(double_letters('javinescula'), double_letters('javinescula') is False)
print(double_letters('margarina'), double_letters('margarina') is False)
print(double_letters('cacetinho'), double_letters('cacetinho') is False)
print(double_letters('café'), double_letters('café') is False)
print(double_letters('happy'), double_letters('happy') is True)
