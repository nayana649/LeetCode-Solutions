class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
            
        result = []
        # Use a standard list as a LIFO stack
        stack = [root]
        
        while stack:
            # Pop the current node (Root)
            node = stack.pop()
            result.append(node.val)
            
            # Push the right child first so it is processed LATER
            if node.right:
                stack.append(node.right)
                
            # Push the left child second so it sits on top to be processed NEXT
            if node.left:
                stack.append(node.left)
                
        return result