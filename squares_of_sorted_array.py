def sorted_squares(nums):
    def split_and_square(nums):
        if not nums:
            return [], []

        head = nums[0]
        tail = nums[1:]

        left, right = split_and_square(tail)
        if head < 0:
            return [head * head] + left, right
        else:
            return left, [head * head] + right

    def reverse(arr):
        if not arr:
            return []
        return reverse(arr[1:]) + [arr[0]]

    def merge(a, b):
        if not a:
            return b
        if not b:
            return a
        if a[0] < b[0]:
            return [a[0]] + merge(a[1:], b)
        else:
            return [b[0]] + merge(a, b[1:])


    neg_squares, pos_squares = split_and_square(nums)
    neg_squares = reverse(neg_squares)
    return merge(neg_squares, pos_squares)
