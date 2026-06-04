class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
            
        # dp[i] will store the minimum cuts needed for prefix s[0...i]
        # Max cuts possible for a string of length i is i cuts (cutting every character)
        dp = [i for i in range(n)]
        
        def expand_around_center(left: int, right: int):
            # Expand outward as long as the substring remains a palindrome
            while left >= 0 and right < n and s[left] == s[right]:
                if left == 0:
                    # If the palindrome starts at index 0, no cuts are needed at all
                    dp[right] = 0
                else:
                    # Otherwise, cuts = (cuts needed before this palindrome) + 1 cut
                    dp[right] = min(dp[right], dp[left - 1] + 1)
                
                left -= 1
                right += 1

        # Evaluate every index as a potential palindrome center
        for i in range(n):
            expand_around_center(i, i)      # Odd-length palindromes (e.g., "aba")
            expand_around_center(i, i + 1)  # Even-length palindromes (e.g., "abba")
            
        return dp[n - 1]