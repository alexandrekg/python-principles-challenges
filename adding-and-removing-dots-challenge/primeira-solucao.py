def add_dots(word):
    return ".".join(word)


def remove_dots(word):
    return "".join(word.split("."))


print(add_dots("test"), add_dots("test") == "t.e.s.t")
print(add_dots("hello"), add_dots("hello") == "h.e.l.l.o")
print(add_dots("start"), add_dots("start") == "s.t.a.r.t")

print(remove_dots("s.t.a.r.t"), remove_dots("s.t.a.r.t") == "start")
print(remove_dots("h.e.l.l.o"), remove_dots("h.e.l.l.o") == "hello")
print(remove_dots("t.e.s.t"), remove_dots("t.e.s.t") == "test")
