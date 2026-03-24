from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = 0
        dp = dict()
        def f(nums, indx):
            if indx >= len(nums): return 0
            if indx in dp : return dp[indx]

            #skip
            skip = f(nums,indx+1)
            take = nums[indx] + f(nums,indx+2)
            dp[indx] = max(skip,take)
            return max(skip,take)
        return f(nums,0)
    
    
    # bottom up approach
    
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        ans = [0]*len(nums)
        ans[0] = nums[0]
        ans[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            ans[i] = max(ans[i-1],nums[i] + ans[i-2])
        return ans[len(nums)-1]
        
# space optimized approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = 0
        dp = dict()
        dp[len(nums)] = 0
        dp[len(nums)-1] = nums[len(nums)-1]
        for ind in range(len(nums)-2,-1,-1):
            skip = dp[ind+1]
            take = nums[ind] + dp[ind+2]
            dp[ind] = max(skip,take)
        return dp[0]