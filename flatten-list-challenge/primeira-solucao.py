def flatten(lists: list):
    new_list = []
    for l in lists:
        new_list.extend(l)
    return new_list


print(flatten([[1, 2], [3, 4]]), flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4])