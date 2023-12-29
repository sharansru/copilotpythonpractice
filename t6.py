def find_max(arr):
    m = arr[0]

    for a in arr:
        if m < a:
            m = a

    return m

numbers = [5, 12, -3, 8, 1, 9, 5, -1]

max_number = find_max(numbers)
print(f"The maximum element in the array is: {max_number}")
