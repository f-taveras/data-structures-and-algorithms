def insert_shift_array(arr, value):
    middle_index = len(arr) // 2 if len(arr) % 2 == 0 else (len(arr) + 1) // 2
    

    new_arr = []

    for i in range(len(arr) + 1):
        if i == middle_index:
            new_arr.append(value)

        if i < len(arr):
            new_arr.append(arr[i])

    return new_arr

test_array = [1, 2, 3, 4, 5]
new_value = 3
result = insert_shift_array(test_array, new_value)
print(result)