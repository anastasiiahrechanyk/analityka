def merge(nums1, m, nums2, n):
    def helper(i, j, k):
        if j < 0:
            return  
        if i < 0:
            
            nums1[k] = nums2[j]
            helper(i, j - 1, k - 1)
        elif nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            helper(i - 1, j, k - 1)
        else:
            nums1[k] = nums2[j]
            helper(i, j - 1, k - 1)

    helper(m - 1, n - 1, m + n - 1)
