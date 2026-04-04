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