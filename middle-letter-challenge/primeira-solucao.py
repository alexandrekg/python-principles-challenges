def mid(word):
    if len(word) % 2 == 0:
        return ""
    
    return word[round(len(word) / 2) - 1]

print(mid("abc"), mid("abc") == "b")
print(mid("abcd"), mid("abcd") == "")