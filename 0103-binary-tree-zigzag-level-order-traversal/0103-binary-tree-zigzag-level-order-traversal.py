from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
            
        result = []
        queue = deque([root])
        left_to_right = True  # Flag to track traversal direction
        
        while queue:
            level_size = len(queue)
            # Pre-allocate the list for the current level to insert by index directly
            current_level = [0] * level_size
            
            for i in range(level_size):
                node = queue.popleft()
                
                # Determine position based on current direction flag
                index = i if left_to_right else (level_size - 1 - i)
                current_level[index] = node.val
                
                # Always enqueue children in standard left-to-right order
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
            left_to_right = not left_to_right  # Alternate direction for the next level
            
        return result