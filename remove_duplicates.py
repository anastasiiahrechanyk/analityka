def remove_duplicates(nums):
    def helper(index, write_index):
        if index == len(nums):
            return write_index
        if nums[index] != nums[write_index - 1]:
            nums[write_index] = nums[index]
            return helper(index + 1, write_index + 1)
        else:
            return helper(index + 1, write_index)

    if not nums:
        return 0
    return helper(1, 1)
