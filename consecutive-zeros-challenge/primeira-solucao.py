def consecutive_zeros(binary_str):
    return len(max(binary_str.split('1')))


print(consecutive_zeros("1001101000110"))