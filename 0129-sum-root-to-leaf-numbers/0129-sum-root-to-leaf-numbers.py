class Solution:
    def sumNumbers(self, root: 'TreeNode | None') -> int:
        
        def dfs(node: 'TreeNode | None', current_number: int) -> int:
            # Base case: if the branch is empty, it contributes 0 to the total sum
            if not node:
                return 0
            
            # Update the number representing the current path
            current_number = current_number * 10 + node.val
            
            # If we reach a leaf node, return the completed path number
            if not node.left and not node.right:
                return current_number
                
            # Otherwise, continue down both subtrees and sum their results
            left_sum = dfs(node.left, current_number)
            right_sum = dfs(node.right, current_number)
            
            return left_sum + right_sum
            
        return dfs(root, 0)