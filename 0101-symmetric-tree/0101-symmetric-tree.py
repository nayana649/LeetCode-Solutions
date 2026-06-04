from collections import deque

class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True
            
        # Initialize a queue with the left and right children of the root
        queue = deque([(root.left, root.right)])
        
        while queue:
            t1, t2 = queue.popleft()
            
            # If both are null, this mirror path is valid; keep going
            if not t1 and not t2:
                continue
            # If only one is null or the values misalign, it's asymmetric
            if not t1 or not t2 or t1.val != t2.val:
                return False
                
            # Push corresponding mirroring pairs together into the queue
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))
            
        return True