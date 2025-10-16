def valid_mountain_array(arr):
    if len(arr) < 3:
        return False

    def climb_up(i):
        if i + 1 >= len(arr):
            return i
        if arr[i] < arr[i + 1]:
            return climb_up(i + 1)
        return i

    def climb_down(i):
        if i + 1 >= len(arr):
            return i == len(arr) - 1
        if arr[i] > arr[i + 1]:
            return climb_down(i + 1)
        return False

    peak = climb_up(0)

    if peak == 0 or peak == len(arr) - 1:
        return False

    return climb_down(peak)
