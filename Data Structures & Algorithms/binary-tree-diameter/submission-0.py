# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # brute force - DFS on each node
        # but this is a binary tree and BFS may have a better way
        # if we know the max depth at each level for each side we 
        # can just sum up the node that has the max of left + right

        # keep track of l and r
        node_map = {}

        cur = root
        
        def dfs(cur):
            l = r = 0
            if cur.left:
                l = dfs(cur.left)
            if cur.right:
                r = dfs(cur.right)

            node_map[cur.val] = l + r
            return max(l, r) + 1

        dfs(cur)
        return max(node_map.values())
                
