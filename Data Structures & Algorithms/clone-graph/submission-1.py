"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        stack = [node]
        old_to_new = {node: Node(node.val)}
        while stack:
            current = stack.pop()
            for neighbor in current.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                old_to_new[current].neighbors.append(old_to_new[neighbor])
        return old_to_new[node]
        