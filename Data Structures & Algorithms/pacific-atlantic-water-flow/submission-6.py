class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # we will try to get to all possible cells from a valid edge
        # we have 2 sets and if a cell is in both then it is fully valid

        valid1 = []
        valid2 = [False] * len(heights[0])

        pac = set()
        atl = set()

        def dfs(x, y, set_t):
            set_t.add((x,y))
            neighbors = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]

            for n in neighbors:
                # go to neighbors if they are correct height and valid
                if n[0] >= 0 and n[0] < len(heights) and n[1] >= 0 and n[1] < len(heights[0]):
                    if (n[0], n[1]) not in set_t:
                        if heights[x][y] <= heights[n[0]][n[1]]:
                            dfs(n[0], n[1], set_t)


        for i in range(len(heights[0])):
            # pacific
            dfs(0, i, pac)

            # atlantic
            dfs(len(heights)-1, i, atl)

        for i in range(len(heights)):
            # pacific
            dfs(i, 0, pac)

            # atlantic
            dfs(i, len(heights[0])-1, atl)

        res = pac & atl
        return [[x, y] for x, y in res]
        
        
        