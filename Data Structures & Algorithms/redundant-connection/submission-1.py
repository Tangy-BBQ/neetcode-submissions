class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # we are starting with an edge list
        # some useful tools could be an adjacency matrix
        # or we may need to traverse the graph and see what has been visited
        # the problem with the traversal is that we need to maintain certain properties

        # we can determine the cycle nodes easily through either the list or an adjacency matrix
        # can we just keep a count of appearances? not really
        # we only have ONE extra edge

        # we could check if our graph is valid when removing EACH edge
        # this seems slow

        # keep a parent list for each node
        par = [i for i in range(len(edges) + 1)]

        # we also keep track of our rank
        rank = [1] * (len(edges) + 1)
        
        def find(n):
            if n == par[n]:
                return n
            par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            