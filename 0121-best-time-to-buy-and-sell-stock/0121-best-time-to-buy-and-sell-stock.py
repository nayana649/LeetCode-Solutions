class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Initialize min_price to infinity so any first day price updates it
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update the minimum price seen so far (potential buy day)
            if price < min_price:
                min_price = price
            # Otherwise, check if selling today yields a higher profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit