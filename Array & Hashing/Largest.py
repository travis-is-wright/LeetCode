def get_largest(values):
    if len(values) == 0:
        return 0

    int_array = []
    for i in range(len(values) - 1, -1, -1):
        int_array.append(values[i])
    return int_array


list_values = [0, 2, 4, 6, 10, 12, 2, 265]
print(get_largest(list_values))

