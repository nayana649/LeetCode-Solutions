from collections import deque

class Solution:
    def minDepth(self, root: 'TreeNode | None') -> int:
        # Base Case: An empty tree has a depth of 0
        if not root:
            return 0
            
        # Queue stores pairs of (node, current_depth)
        queue = deque([(root, 1)])
        
        while queue:
            node, depth = queue.popleft()
            
            # The first leaf node we encounter gives us the minimum depth
            if not node.left and not node.right:
                return depth
                
            # Expand to children nodes if they exist
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
                
        return 0