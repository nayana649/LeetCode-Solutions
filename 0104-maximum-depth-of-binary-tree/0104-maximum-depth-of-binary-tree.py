# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        # Base Case: An empty node contributes 0 to the depth
        if not root:
            return 0
            
        # Divide: Recursively find the depth of both subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Conquer: The depth of the current node is 1 + the max depth of its children
        return max(left_depth, right_depth) + 1