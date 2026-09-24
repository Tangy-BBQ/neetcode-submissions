"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # we can just do a dfs with reconstruction
        # we need to know what we have visited so far

        if not node:
            return None

        node_map = {}

        def dfs(cur, parent):
            # visited.append(cur.val)
            # print(cur.val)
            new_cur = Node(val = cur.val)
            new_neighbors = []
            node_map[cur.val] = new_cur
            if parent:
                new_neighbors.append(parent)
            for n in cur.neighbors:
                if n.val not in node_map:
                    new_neighbors.append(dfs(n, new_cur))
                elif (parent and n.val != parent.val) or not parent:
                    # we already created this node
                    new_neighbors.append(node_map[n.val])
                # else:
                #     print("skipping", n.val, parent.val if parent else "")

            new_cur.neighbors = new_neighbors
            # print(cur.val)
            # print([n.val for n in cur.neighbors])
            # print([n.val for n in new_cur.neighbors])
            # print()
            # visited.pop()
            return new_cur

        return dfs(node, None)
        