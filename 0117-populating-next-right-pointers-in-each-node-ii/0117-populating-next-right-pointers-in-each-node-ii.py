class Solution:
    def connect(self, root: 'Node' = None) -> 'Node':
        if not root:
            return None
            
        # 'curr_level_start' tracks the first node of the level we are currently processing
        curr_level_start = root
        
        while curr_level_start:
            # Dummy node acts as a prefix anchor for the next level's linked list
            dummy = Node(0)
            tail = dummy  # tail will append nodes to the next level's list
            
            # 'curr' walks across the current level using its pre-established .next links
            curr = curr_level_start
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                    
                # Move horizontally to the next parent node
                curr = curr.next
                
            # Move down to the start of the newly constructed level list
            curr_level_start = dummy.next
            
        return root