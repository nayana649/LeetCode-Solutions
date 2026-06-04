from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
            
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            # Process all nodes belonging strictly to the current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # Enqueue children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Append the completed level list to our final matrix
            result.append(current_level)
            
        return result