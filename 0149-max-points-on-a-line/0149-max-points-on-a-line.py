import math
from collections import defaultdict

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n  # Any 1 or 2 points will always form a straight line
            
        max_total_points = 0
        
        for i in range(n):
            slopes = defaultdict(int)
            local_max = 0
            x1, y1 = points[i]
            
            # Compare anchor point 'i' with all subsequent points 'j'
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                dy = y2 - y1
                dx = x2 - x1
                
                # Simplify the fraction using the greatest common divisor
                g = math.gcd(dy, dx)
                dy //= g
                dx //= g
                
                # Normalize representation for consistency (e.g., handles negative slopes cleanly)
                if dx < 0 or (dx == 0 and dy < 0):
                    dy = -dy
                    dx = -dx
                    
                slope_key = (dy, dx)
                slopes[slope_key] += 1
                
                # Keep track of the most frequent slope from this anchor
                if slopes[slope_key] > local_max:
                    local_max = slopes[slope_key]
            
            # The number of collinear points is local_max + 1 (to include the anchor itself)
            max_total_points = max(max_total_points, local_max + 1)
            
        return max_total_points