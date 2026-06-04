from functools import cache

class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []
            
        @cache
        def build_trees(start: int, end: int):
            if start > end:
                return [None]
                
            all_trees = []
            
            for i in range(start, end + 1):
                left_trees = build_trees(start, i - 1)
                right_trees = build_trees(i + 1, end)
                
                for left in left_trees:
                    for right in right_trees:
                        # Uses LeetCode's built-in TreeNode automatically
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
                        
            return all_trees
            
        return build_trees(1, n)