def count(word):
    return len(word.split('-'))


print(count("te-st"), count("te-st") == 2)
print(count("ho-tel"), count("ho-tel") == 2)
print(count("cat"), count("cat") == 1)
