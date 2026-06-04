class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        # Start from the second-to-last row and move upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Add the minimum of the two adjacent children from the row below
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
                
        # The apex now contains the minimum path sum
        return triangle[0][0]