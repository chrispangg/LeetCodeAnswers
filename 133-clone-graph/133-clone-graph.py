"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        copyList = {None: None}
        
        def dfs(node):
            if node in copyList:
                return copyList[node]
            
            copy = Node(node.val, [])
            copyList[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy
        
        return dfs(node) if node else None
        
        
        
        