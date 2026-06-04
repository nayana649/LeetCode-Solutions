class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        total_profit = 0
        
        # Start from the second day (index 1) to compare with the previous day
        for i in range(1, len(prices)):
            # If the price increased compared to yesterday, lock in the profit
            if prices[i] > prices[i-1]:
                total_profit += prices[i] - prices[i-1]
                
        return total_profit