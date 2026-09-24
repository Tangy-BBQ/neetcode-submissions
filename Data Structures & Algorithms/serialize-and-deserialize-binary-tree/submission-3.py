from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return ""

        # Using deque for efficient O(1) pops from the front
        queue = deque([root])
        serialized = [root.val]

        while queue:
            cur = queue.popleft()

            if cur.left:
                serialized.append(cur.left.val)
                queue.append(cur.left)
            else:
                serialized.append(None)

            if cur.right:
                serialized.append(cur.right.val)
                queue.append(cur.right)
            else:
                serialized.append(None)
                
        return ",".join(str(x) for x in serialized)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
            
        # Convert split data into a deque for fast processing
        data_deque = deque(data.split(","))
        
        root = TreeNode(int(data_deque.popleft()))
        queue = deque([root])
        
        # Keep processing as long as we have nodes to build and data left to read
        while queue and data_deque:
            cur = queue.popleft()
            
            l = "None"
            r = "None"
            
            if data_deque:
                l = data_deque.popleft()
            if data_deque:
                r = data_deque.popleft()
                
            if l != "None":
                cur.left = TreeNode(int(l))
                queue.append(cur.left)
            if r != "None":
                cur.right = TreeNode(int(r))
                queue.append(cur.right)
        
        return root