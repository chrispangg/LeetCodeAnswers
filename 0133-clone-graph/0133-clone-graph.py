"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        visited = {None: None}
        
        def dfs(node):
            if node in visited:
                return visited[node]
            
            newNode = Node(node.val, None)
            
            visited[node] = newNode
            
            for n in node.neighbors:
                newNode.neighbors.append(dfs(n))
        
            return newNode
        
        return dfs(node) if node else None
        
            