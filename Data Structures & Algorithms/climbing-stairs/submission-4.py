class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n+1)
        def helper(num):
            if num <= 1:
                return 1
            if dp[num] != 1:
                return dp[num]
            dp[num] = helper(num-1) + helper(num-2)
            return dp[num]
        return helper(n)
        

       

        