def get_row_col(_str):
    translate = {'A': 0, 'B': 1, 'C': 2}
    row = int(_str[1]) - 1
    column = translate[_str[0]]
    return (row, column)

print(get_row_col('A3'))