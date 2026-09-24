class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a tree is a vertical non cyclical structure
        # if a node is a parent, none of its children or lower may be a parent or sibling
        # we should be able to check in O(edges)
        # how to best do this?
        # we could build the tree and check for cycles which should be O(n) + O(edges)
        # we also need to verify no islands
        # a node can only have one parent but any number of children
        # we dont know which is which
        # we should be able to run dfs and never visit the same node twice
        # as long as we dont go back to our parent

        # def node(val, children):
        #     self.val = val
        #     self.children = children

        nodes = {}

        # for i in range(n):


        for (e1, e2) in edges:
            nodes[e1] = nodes.get(e1, []) + [e2]
            nodes[e2] = nodes.get(e2, []) + [e1]
        print(nodes)

        for cur in nodes.keys():
            if nodes.get(cur, []) == []:
                # print('len')
                return False

        def dfs(node, parent, visited):
            all_vis.add(node)
            if node in visited:
                # print('vis')
                return False
            val = True
            for child in nodes.get(node, []):
                if child != parent:
                    visited.append(node)
                    val = val and dfs(child, node, visited)
                    visited.pop()
            return val
        
        all_vis = set()
        res = dfs(0, None, [])
        # print(len(all_vis), n)
        # print(all_vis, len(all_vis) == n, res)
        return len(all_vis) == n and res
