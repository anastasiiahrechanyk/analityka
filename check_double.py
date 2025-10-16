def check_if_exist(arr):
    def check_pair(i, j):
        if j == len(arr):
            return False
        if i != j and arr[i] == 2 * arr[j]:
            return True
        return check_pair(i, j + 1)

    def outer(i):
        if i == len(arr):
            return False
        if check_pair(i, 0):
            return True
        return outer(i + 1)

    return outer(0)
