class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Convert the list to a set to enable O(1) lookups
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # Check if 'num' is the start of a consecutive sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Incrementally look for the next elements of the chain
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                    
                # Keep track of the maximum sequence length seen so far
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak