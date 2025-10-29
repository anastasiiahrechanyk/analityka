from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        for i, n in enumerate(nums):
            while dq and nums[dq[-1]] < n:
                dq.pop()
            dq.append(i)
            if dq[0] == i - k:
                dq.popleft()
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    print(s.maxSlidingWindow([1], 1)) 
