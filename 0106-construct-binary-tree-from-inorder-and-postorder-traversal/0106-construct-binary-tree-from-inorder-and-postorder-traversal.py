class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> 'TreeNode | None':
        # Create a hash map for O(1) index lookups of values inside the inorder array
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Start our pointer at the end of the postorder array (the absolute root)
        post_idx = len(postorder) - 1
        
        def array_to_tree(in_start: int, in_end: int):
            nonlocal post_idx
            
            # Base Case: No elements left to process in this subtree's inorder range
            if in_start > in_end:
                return None
                
            # Pick the current element from postorder as the root node
            root_val = postorder[post_idx]
            root = TreeNode(root_val)
            post_idx -= 1
            
            # Find where this root splits the inorder sequence
            pivot = inorder_map[root_val]
            
            # CRITICAL STEP: Build the right subtree first!
            # Since we are scanning postorder backward, the right child comes right before the root
            root.right = array_to_tree(pivot + 1, in_end)
            root.left = array_to_tree(in_start, pivot - 1)
            
            return root
            
        return array_to_tree(0, len(inorder) - 1)