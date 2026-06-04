class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> 'TreeNode | None':
        
        def convert(left: int, right: int) -> 'TreeNode | None':
            # Base Case: If the boundaries cross, there are no elements left to process
            if left > right:
                return None
                
            # Choose the middle element as the root to maintain height balance
            mid = (left + right) // 2
            
            # Create the node with the middle value
            root = TreeNode(nums[mid])
            
            # Recursively build the left and right subtrees from split halves
            root.left = convert(left, mid - 1)
            root.right = convert(mid + 1, right)
            
            return root
            
        return convert(0, len(nums) - 1)