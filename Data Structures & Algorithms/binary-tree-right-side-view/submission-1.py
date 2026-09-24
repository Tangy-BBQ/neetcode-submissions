# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # the question is basically BFS
        # we need to only return the right most for each level
        # we will traverse in right to left and only append the FIRST for each level
        if not root:
            return []
        # level = 0
        found_at_level = {}
        queue = [(root, 0)]
        rights = []

        while queue:
            cur, level = queue.pop()
            # print(cur.val)

            if not found_at_level.get(level, False):
                rights.append(cur.val)
                found_at_level[level] = True
            if cur.left:
                queue.append((cur.left, level + 1))
            if cur.right:
                queue.append((cur.right, level + 1))
        return rights

        