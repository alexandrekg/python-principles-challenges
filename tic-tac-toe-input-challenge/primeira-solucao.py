def get_row_col(_str):
    translate_columns = [
        ('A', 0),
        ('B', 1),
        ('C', 2)
    ]

    translate_rows = [
        ('1', 0),
        ('2', 1),
        ('3', 2)
    ]

    for t_row in translate_rows:
        if t_row[0] == _str[1]:
            row = t_row[1]

    for t_col in translate_columns:
        if t_col[0] in _str[0]:
            column = t_col[1]
    return (row, column)


print(get_row_col('A3'))