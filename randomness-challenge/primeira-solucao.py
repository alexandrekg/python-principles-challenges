import random

def random_number():
    return random.randint(1, 100)

r_number = random_number()
print(r_number, 100 >= r_number >= 1)