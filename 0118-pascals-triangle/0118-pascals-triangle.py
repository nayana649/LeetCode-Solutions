class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # Initialize the triangle with the first row
        triangle = [[1]]
        
        # Build from the second row up to numRows
        for i in range(1, numRows):
            prev_row = triangle[-1]
            # Start the new row with a 1
            current_row = [1]
            
            # Compute the mathematical sum for the internal elements
            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])
                
            # End the new row with a 1
            current_row.append(1)
            
            # Append the completed row to our triangle matrix
            triangle.append(current_row)
            
        return triangle