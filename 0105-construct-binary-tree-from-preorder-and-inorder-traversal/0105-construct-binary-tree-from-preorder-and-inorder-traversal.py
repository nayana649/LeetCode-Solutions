class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> 'TreeNode | None':
        # Create a hash map for O(1) index lookups of values inside the inorder array
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Pointer to track our position as we read across the preorder array
        pre_idx = 0
        
        def array_to_tree(in_start: int, in_end: int):
            nonlocal pre_idx
            
            # Base Case: No elements left in this subtree's inorder range
            if in_start > in_end:
                return None
                
            # Pick the current element from preorder as the root node
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)  # This will now correctly use LeetCode's built-in class
            pre_idx += 1
            
            # Find where this root splits the inorder sequence
            pivot = inorder_map[root_val]
            
            # Build subtrees
            root.left = array_to_tree(in_start, pivot - 1)
            root.right = array_to_tree(pivot + 1, in_end)
            
            return root
            
        return array_to_tree(0, len(inorder) - 1)