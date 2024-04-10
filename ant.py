def find_x(arr):
    last_index = -1

    for i, num in enumerate(arr):
        if num != -1:
            last_index = i

        elif last_index >= 0:
            return i

    return last_index + 1

input_str = input("Enter the elements: ")
arr = [int(num) for num in input_str.split()]

index_x = find_x(arr)

print(f"Index x : {index_x}")