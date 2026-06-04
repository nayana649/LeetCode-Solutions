class Solution:
    def connect(self, root: 'Node' = None) -> 'Node':
        if not root:
            return None
            
        # Start with the absolute root of the tree
        leftmost = root
        
        # Loop down level by level. Stop when we reach a leaf level 
        # because leaves don't have children to establish links for.
        while leftmost.left:
            
            # Slide horizontally across the current level using 'curr'
            curr = leftmost
            while curr:
                # Connection 1: Link left child to right child under the same parent
                curr.left.next = curr.right
                
                # Connection 2: Link right child to the neighbor's left child
                if curr.next:
                    curr.right.next = curr.next.left
                    
                # Move horizontally to the next node on the same level
                curr = curr.next
                
            # Move down to the start of the next level
            leftmost = leftmost.left
            
        return root