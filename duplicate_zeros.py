def duplicate_zeros(arr):
    def helper(i, extra_insertions):
        if i == len(arr) - 1:
            return

        helper(i + 1, extra_insertions + (1 if arr[i] == 0 else 0))

        if arr[i] == 0:
            shift(i + extra_insertions, 0)
            shift(i + extra_insertions - 1, 0)
        else:
            shift(i + extra_insertions, arr[i])

    def shift(index, value):
        if 0 <= index < len(arr):
            arr[index] = value

    helper(0, 0)

if __name__ == "__main__":
    arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
    duplicate_яeros(arr1)
    print("Output:", arr1)

    arr2 = [1, 2, 3]
    duplicate_zeros(arr2)
    print("Output:", arr2)

    arr3 = [0, 0, 0, 0, 0, 0, 0]
    duplicate_zeros(arr3)
    print("Output:", arr3)
