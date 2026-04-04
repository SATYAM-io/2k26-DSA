class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = dict()
        def f(coins, ind,amt):
            if amt ==0: return 0
            if ind >= len(coins):return 999999
            if (ind, amt) in dp : return dp[(ind, amt)]

            skip = f(coins, ind+1, amt)
            take = 999999
            if amt>=coins[ind]:
                take = 1+f(coins, ind, amt-coins[ind])
            dp[(ind, amt)] = min(take,skip)
            return  dp[(ind, amt)] 
        
        ans = f(coins,0,amount)
        if ans > amount: return -1
        return ans