class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        current_partition = []
        
        def is_palindrome(substring: str) -> bool:
            # Simple two-pointer check for palindrome validation
            left, right = 0, len(substring) - 1
            while left < right:
                if substring[left] != substring[right]:
                    return False
                left += 1
                right -= 1
            return True
            
        def backtrack(start_idx: int):
            # If we've processed the entire string, a valid partition is complete
            if start_idx == len(s):
                result.append(list(current_partition))
                return
                
            # Explore all possible cut positions from the current start index
            for end_idx in range(start_idx + 1, len(s) + 1):
                substring = s[start_idx:end_idx]
                
                # Only proceed down this branch if the current substring is a palindrome
                if is_palindrome(substring):
                    current_partition.append(substring)  # Choose
                    backtrack(end_idx)                  # Explore
                    current_partition.pop()             # Backtrack (Unchoose)
                    
        backtrack(0)
        return result