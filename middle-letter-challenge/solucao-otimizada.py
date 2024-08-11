def mid(word):
    if len(word) % 2 == 0:
        return ""
    
    return word[len(word) // 2]

print(mid("abc"), mid("abc") == "b")
print(mid("abcd"), mid("abcd") == "")