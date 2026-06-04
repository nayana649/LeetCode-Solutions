class Solution:
    def hasPathSum(self, root: 'TreeNode | None', targetSum: int) -> bool:
        # Base Case 1: If the tree or branch is empty, no path exists
        if not root:
            return False
            
        # Base Case 2: If we are at a leaf node, check if its value matches the remaining sum
        if not root.left and not root.right:
            return root.val == targetSum
            
        # Recursive Step: Subtract the current node's value from targetSum
        # and check both left and right subtrees
        remaining_sum = targetSum - root.val
        return (self.hasPathSum(root.left, remaining_sum) or 
                self.hasPathSum(root.right, remaining_sum))