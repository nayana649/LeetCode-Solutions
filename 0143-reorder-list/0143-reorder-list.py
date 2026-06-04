class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        # Phase 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 'slow' is now at the midpoint. Split the list into two halves.
        second_half = slow.next
        slow.next = None  # Sever the connection to terminate the first half
        
        # Phase 2: Reverse the second half in-place
        prev = None
        curr = second_half
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # 'prev' now points to the head of the reversed second half
        first_half = head
        second_half = prev
        
        # Phase 3: Interleave/Weave the two halves together
        while second_half:
            # Save the next pointer positions
            temp1 = first_half.next
            temp2 = second_half.next
            
            # Wire the nodes together
            first_half.next = second_half
            second_half.next = temp1
            
            # Shift pointers forward for the next iteration step
            first_half = temp1
            second_half = temp2