class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # need to keep track of all pieces of a whole component
        # can keep a list of pieces
        # for each new edge we can check if one of the edges already exists in a component
        # if it does not then we add both to a component
        # problem is then to condense down any components that share an edge not seen before

        # could make a list of maps, each index corresponds to a node and its value is a map of all of its edges

        nmaps = [set() for _ in range(n)]

        for i in range(len(edges)):
            v1, v2 = edges[i][0], edges[i][1]

            nmaps[v1].add(v2)
            nmaps[v2].add(v1)

            # print(nmaps)



        def dfs(cur, visited):
            if cur in visited:
                return 0
            visited.add(cur)

            for i in nmaps[cur]:
                dfs(i, visited)
            return 1

        count = 0
        visited = set()
        for i in range(n):
            count = count + dfs(i, visited) 

        return count
        