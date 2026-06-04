# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = second = prev = None
        curr = root
        
        while curr:
            if not curr.left:
                # --- Process the Node (Inorder Position) ---
                if prev and prev.val > curr.val:
                    if not first:
                        first = prev  # First anomaly is the larger value
                    second = curr     # Second anomaly is the smaller value
                prev = curr
                # --------------------------------------------
                curr = curr.right
            else:
                # Find the inorder predecessor of curr
                predecessor = curr.left
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right
                
                # Make curr the right child of its predecessor (Establish temporary bridge)
                if not predecessor.right:
                    predecessor.right = curr
                    curr = curr.left
                else:
                    # Revert the changes (Break the temporary bridge)
                    predecessor.right = None
                    
                    # --- Process the Node (Inorder Position) ---
                    if prev and prev.val > curr.val:
                        if not first:
                            first = prev
                        second = curr
                    prev = curr
                    # --------------------------------------------
                    
                    curr = curr.right
                    
        # Swap the values of the two mismatched nodes back to normal
        if first and second:
            first.val, second.val = second.val, first.val