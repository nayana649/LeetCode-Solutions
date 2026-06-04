class Solution:
    def maxPathSum(self, root: 'TreeNode | None') -> int:
        # Initialize with negative infinity to handle trees with all negative values
        global_max_sum = float('-inf')
        
        def calculate_gain(node: 'TreeNode | None') -> int:
            nonlocal global_max_sum
            if not node:
                return 0
                
            # Recursively compute the maximum gain from left and right subtrees.
            # If the gain is negative, we greedily skip it by clamping it to 0.
            left_gain = max(0, calculate_gain(node.left))
            right_gain = max(0, calculate_gain(node.right))
            
            # Price out a path that "turns around" at the current node
            current_path_sum = node.val + left_gain + right_gain
            
            # Update our global maximum if this turnaround path is the highest seen
            global_max_sum = max(global_max_sum, current_path_sum)
            
            # Return the maximum single-branch gain this node can offer to its parent
            return node.val + max(left_gain, right_gain)
            
        calculate_gain(root)
        return global_max_sum