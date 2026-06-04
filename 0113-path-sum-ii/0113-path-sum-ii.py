class Solution:
    def pathSum(self, root: 'TreeNode | None', targetSum: int) -> list[list[int]]:
        result = []
        
        def dfs(node: 'TreeNode | None', remaining_sum: int, current_path: list[int]):
            if not node:
                return
                
            # Choose: Add the current node's value to our path tracking list
            current_path.append(node.val)
            
            # Check if it's a leaf node and if it satisfies the remaining target sum
            if not node.left and not node.right and node.val == remaining_sum:
                # Append a copy of current_path since lists are passed by reference
                result.append(list(current_path))
            else:
                # Explore: Continue down both branches with the updated sum
                dfs(node.left, remaining_sum - node.val, current_path)
                dfs(node.right, remaining_sum - node.val, current_path)
                
            # Backtrack: Remove the current node's value before returning up the tree
            current_path.pop()
            
        dfs(root, targetSum, [])
        return result