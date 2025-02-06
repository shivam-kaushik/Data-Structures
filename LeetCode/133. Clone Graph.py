"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        node_map = {}

        queue = deque([node])
        node_map[node] = Node(node.val)

        while queue:
            current_node = queue.popleft()
            for neighbor in current_node.neighbors:
                if neighbor not in node_map:
                    node_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                node_map[current_node].neighbors.append(node_map[neighbor])

        return node_map[node]