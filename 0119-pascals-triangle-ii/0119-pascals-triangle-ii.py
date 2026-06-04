class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        # Initialize an array of 1s of the exact required size
        row = [1] * (rowIndex + 1)
        
        # Build the rows sequentially up to rowIndex
        for i in range(1, rowIndex):
            # Iterate backward from right to left to avoid overwriting previous data
            for j in range(i, 0, -1):
                row[j] = row[j] + row[j-1]
                
        return row