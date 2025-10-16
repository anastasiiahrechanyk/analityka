def count_even_digit_numbers(nums):
    def count_digits(n):
        if n < 10:
            return 1
        return 1 + count_digits(n // 10)

    def helper(index):
        if index == len(nums):
            return 0
        digits = count_digits(nums[index])
        add = 1 if digits % 2 == 0 else 0
        return add + helper(index + 1)

    return helper(0)

if __name__ == "__main__":
    nums1 = [12, 345, 2, 6, 7896]
    nums2 = [555, 901, 482, 1771]
    nums3 = [1, 22, 333, 4444, 55555]

    print("Input:", nums1)
    print("Output:", count_even_digit_numbers(nums1))

    print("Input:", nums2)
    print("Output:", count_even_digit_numbers(nums2))

    print("Input:", nums3)
    print("Output:", count_even_digit_numbers(nums3))
