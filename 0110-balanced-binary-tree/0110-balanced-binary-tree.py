class Solution:
    def isBalanced(self, root: 'TreeNode | None') -> bool:
        
        def check_height(node: 'TreeNode | None') -> int:
            # Base Case: An empty node has a height of 0
            if not node:
                return 0
            
            # Check the height of the left subtree
            left_height = check_height(node.left)
            if left_height == -1:
                return -1  # Left subtree is already unbalanced
                
            # Check the height of the right subtree
            right_height = check_height(node.right)
            if right_height == -1:
                return -1  # Right subtree is already unbalanced
                
            # If the current node violates the balance condition, return -1
            if abs(left_height - right_height) > 1:
                return -1
                
            # Otherwise, return the actual height of this node's subtree
            return max(left_height, right_height) + 1
            
        # If check_height returns -1, the tree is unbalanced; otherwise it's balanced
        return check_height(root) != -1