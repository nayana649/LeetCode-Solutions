class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        
        # Iterate through every bit position from 0 to 31
        for i in range(32):
            bit_sum = 0
            # Count how many numbers have the i-th bit set to 1
            for num in nums:
                # Use a bitmask to isolate the i-th bit
                if (num >> i) & 1:
                    bit_sum += 1
            
            # The bit of our single number is the remainder when divided by 3
            bit_val = bit_sum % 3
            
            # Set the i-th bit in our result
            result |= (bit_val << i)
            
        # If the 31st bit (sign bit) is set, convert back to a negative 32-bit signed int
        if result >= 2**31:
            result -= 2**32
            
        return result