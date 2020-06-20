
# climb n stairs, how many ways?
def climbStairs(self, n: int) -> int:
        memo = {}
        memo[0] = 1
        
        def helper(n):
            if n in memo:
                return memo[n]
            if n < 0:
                return 0

            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]
        
        return helper(n)