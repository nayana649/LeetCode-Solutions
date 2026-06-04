class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        # Step 1: Find the length of the linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        dummy = ListNode(0)
        dummy.next = head
        step = 1
        
        # Step 2: Bottom-up merge sub-lists of size 1, 2, 4, 8, ...
        while step < length:
            prev = dummy
            curr = dummy.next
            
            while curr:
                # Split off the first sub-list of size 'step'
                left = curr
                right = self._split(left, step)
                
                # Split off the second sub-list of size 'step' and keep track of the rest
                curr = self._split(right, step)
                
                # Merge the two isolated sub-lists and connect to the sorted chain
                prev.next = self._merge(left, right)
                
                # Fast-forward 'prev' pointer to the end of the newly merged section
                while prev.next:
                    prev = prev.next
                    
            step *= 2
            
        return dummy.next
        
    def _split(self, head: Optional[ListNode], step: int) -> Optional[ListNode]:
        """Splits off a sub-list of a given step size and returns the head of the remainder."""
        curr = head
        for i in range(step - 1):
            if not curr:
                break
            curr = curr.next
            
        if not curr or not curr.next:
            return None
            
        # Disconnect the sub-list from the remainder of the list
        remainder = curr.next
        curr.next = None
        return remainder

    def _merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Standard two-pointer merge function for two sorted linked lists."""
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        tail.next = l1 if l1 else l2
        return dummy.next