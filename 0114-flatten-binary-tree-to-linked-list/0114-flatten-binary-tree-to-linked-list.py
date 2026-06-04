class Solution:
    def flatten(self, root: 'TreeNode | None') -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        
        while curr:
            # If the current node has a left child, we need to relocate it
            if curr.left:
                # Find the rightmost node of the left subtree
                rightmost = curr.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                # Rewire the pointers:
                # 1. Connect the rightmost node of the left subtree to the current right subtree
                rightmost.right = curr.right
                
                # 2. Shift the left subtree to become the right subtree
                curr.right = curr.left
                
                # 3. Explicitly set the left child to None
                curr.left = None
                
            # Move down to the next node on the right
            curr = curr.right