def zap(a, b):
    new_list = []
    count = 0
    while count < len(a):
        new_list.append((a[count], b[count]))
        count += 1

    return new_list


print(zap([1, 2], [3, 4]))