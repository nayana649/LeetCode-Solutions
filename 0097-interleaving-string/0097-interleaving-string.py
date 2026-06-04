class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Step 1: Length Validation
        if len(s1) + len(s2) != len(s3):
            return False
            
        # Ensure s2 is the shorter string if we want strict O(len(s2)) space optimization,
        # though with constraints <= 100, a standard array of size len(s2)+1 is completely fine.
        len1, len2 = len(s1), len(s2)
        
        # dp[j] represents whether s3[:i+j] can be formed by s1[:i] and s2[:j]
        dp = [False] * (len2 + 1)
        
        # Base case: Empty s1 and empty s2 can form an empty s3
        dp[0] = True
        
        # Initialize the 0-th row (matching s3 using ONLY characters from s2)
        for j in range(1, len2 + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
            
        # Fill out the rest of the rows dynamically
        for i in range(1, len1 + 1):
            # Update the 0-th column for the current row (using ONLY characters from s1)
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            
            for j in range(1, len2 + 1):
                # dp[j] on the right side of the assignment is from the previous row (s1 contribution)
                # dp[j-1] is from the current row's left neighbor (s2 contribution)
                match_s1 = dp[j] and s1[i-1] == s3[i+j-1]
                match_s2 = dp[j-1] and s2[j-1] == s3[i+j-1]
                
                dp[j] = match_s1 or match_s2
                
        return dp[len2]