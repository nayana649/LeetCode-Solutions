class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
            
        # Initialize out-of-pocket buy trackers to negative infinity 
        # and profit counters to 0.
        buy1 = float('-inf')
        profit1 = 0
        buy2 = float('-inf')
        profit2 = 0
        
        for price in prices:
            # 1. Best state if we hold our first stock today
            buy1 = max(buy1, -price)
            
            # 2. Best state if we sell our first stock today
            profit1 = max(profit1, buy1 + price)
            
            # 3. Best state if we hold our second stock today (using profit1 reinvestment)
            buy2 = max(buy2, profit1 - price)
            
            # 4. Best state if we sell our second stock today
            profit2 = max(profit2, buy2 + price)
            
        return profit2