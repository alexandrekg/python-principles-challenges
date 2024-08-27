def format_number(num_):
    new_str = []
    count = 0
    for c in str(num_)[::-1]:
        if count == 3:
            new_str.append(',')
            count = 0
        new_str.append(c)
        count += 1


    return "".join(new_str[::-1])

print(format_number(100000))