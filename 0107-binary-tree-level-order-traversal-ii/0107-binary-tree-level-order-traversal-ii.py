from collections import deque

class Solution:
    def levelOrderBottom(self, root: 'TreeNode | None') -> list[list[int]]:
        if not root:
            return []
            
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            # Extract exactly the number of nodes present on this level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # Always enqueue children from left to right
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Append the standard row to our results container
            result.append(current_level)
            
        # Reverse the array of levels to switch from top-down to bottom-up
        return result[::-1]