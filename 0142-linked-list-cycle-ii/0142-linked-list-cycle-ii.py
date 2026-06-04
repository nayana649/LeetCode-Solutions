class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
            
        slow = head
        fast = head
        
        # Step 1: Find if a cycle exists and locate the meeting point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                # Cycle detected! Move one pointer back to the head
                fast = head
                
                # Step 2: Move both pointers at equal speed to find the entry node
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                    
                return slow  # Both pointers meet at the start of the cycle
                
        return None