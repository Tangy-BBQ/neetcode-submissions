# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # a preorder list tells us our first node then the left and right
        # an inorder list tells us left then root then right
        # the main issue we have is in detecting a missing left or right

        # since we have both lists we know our root in both situations
        # we must then check for a discrepancy to detect a missing node
        # the root is also the current pivot in the inorder

        # we will keep track of our node, the preorder, and the inorder index
        root = TreeNode(preorder[0])
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        

        def dfs(p, i, il, ir):
            # we can only investigate between il and ir
            # these represent the half of the previous node we are on
            # everything in these bound is relevant to the current
            # if nothing then we return None

            # create current node
            cur = TreeNode(preorder[p])

            # we will have 0, 1, or 2 children
            if il == ir:
                # we have no children
                return cur
            # if we have 1 which side?
            # well if it is to the left of i
            if il < i:
                # left
                cur.left = dfs(p+1, inorder_map[preorder[p+1]], il, i-1)
            if ir > i:
                # right too
                cur.right = dfs(p+i - il+1, inorder_map[preorder[p+i - il+1]], i+1, ir)
            return cur
                


        root = dfs(0, inorder.index(preorder[0]), 0, len(preorder)-1)
        return root
