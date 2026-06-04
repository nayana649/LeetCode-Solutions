class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[j] stores the number of distinct subsequences of s matching t[0...j-1]
        dp = [0] * (n + 1)
        
        # Base Case: An empty t can always be formed in 1 way
        dp[0] = 1
        
        # Process each character of s
        for i in range(1, m + 1):
            # Traverse backward to use values from the previous row iteration
            for j in range(n, 0, -1):
                if s[i-1] == t[j-1]:
                    # Current ways = (ways without using s[i-1]) + (ways using s[i-1])
                    dp[j] = dp[j] + dp[j-1]
                # If they don't match, dp[j] remains unchanged (dp[i][j] = dp[i-1][j])
                    
        return dp[n]