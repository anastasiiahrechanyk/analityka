from collections import deque
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dq = deque() 
        dp = nums[:] 
        res = nums[0]

        for i in range(len(nums)):
            if dq:
                dp[i] = max(dp[i], nums[i] + dp[dq[0]])
            res = max(res, dp[i])

            while dq and dq[0] < i - k:
                dq.popleft()

            while dq and dp[dq[-1]] <= dp[i]:
                dq.pop()

            dq.append(i)
        
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.constrainedSubsetSum([10, 2, -10, 5, 20], 2))
    print(s.constrainedSubsetSum([-1, -2, -3], 1))        
    print(s.constrainedSubsetSum([10, -2, -10, -5, 20], 2)) 
