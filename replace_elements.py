def replace_elements(arr):
    def helper(index, max_right):
        if index < 0:
            return
        current = arr[index]
        arr[index] = max_right
        helper(index - 1, max(max_right, current))

    helper(len(arr) - 1, -1)
    return arr
