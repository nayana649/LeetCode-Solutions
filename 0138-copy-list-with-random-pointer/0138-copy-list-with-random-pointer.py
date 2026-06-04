class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        # Step 1: Clone each node and insert it right next to the original node
        curr = head
        while curr:
            cloned = Node(curr.val)
            cloned.next = curr.next
            curr.next = cloned
            curr = cloned.next
            
        # Step 2: Assign random pointers for the cloned nodes
        curr = head
        while curr:
            if curr.random:
                # The clone's random pointer should point to the clone of the original random node
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        # Step 3: Separate the interleaved list back into original and copied lists
        curr = head
        cloned_head = head.next
        copy_curr = cloned_head
        
        while curr:
            curr.next = curr.next.next  # Restore original list link
            if copy_curr.next:
                copy_curr.next = copy_curr.next.next  # Link copy list link
                
            curr = curr.next
            copy_curr = copy_curr.next
            
        return cloned_head