def find_max_consecutive_ones(nums):
    def helper(index, current_count, max_count):
        if index == len(nums):
            return max(current_count, max_count)
        if nums[index] == 1:
            return helper(index + 1, current_count + 1, max_count)
        else:
            return helper(index + 1, 0, max(current_count, max_count))

    return helper(0, 0, 0)

if __name__ == "__main__":
    nums1 = [1, 1, 0, 1, 1, 1]
    nums2 = [1, 0, 1, 1, 0, 1]
    nums3 = [0, 0, 0, 0]
    nums4 = [1, 1, 1, 1, 1]

    print("Input:", nums1)
    print("Output:", find_max_consecutive_ones(nums1)) 

    print("Input:", nums2)
    print("Output:", find_max_consecutive_ones(nums2))

    print("Input:", nums3)
    print("Output:", find_max_consecutive_ones(nums3))  

    print("Input:", nums4)
    print("Output:", find_max_consecutive_ones(nums4)) 
