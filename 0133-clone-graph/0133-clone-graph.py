class Solution:
    def cloneGraph(self, node: 'Node' = None) -> 'Node':
        if not node:
            return None
            
        # Hash map to track original_node -> cloned_node mappings
        cloned_map = {}
        
        def dfs(curr_node: 'Node') -> 'Node':
            # If we've already cloned this node, return its cloned instance
            if curr_node in cloned_map:
                return cloned_map[curr_node]
                
            # Create a shallow copy of the node (value copied, neighbors empty)
            copy = Node(curr_node.val)
            cloned_map[curr_node] = copy
            
            # Recursively deep copy all its neighbors
            for neighbor in curr_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
            
        return dfs(node)