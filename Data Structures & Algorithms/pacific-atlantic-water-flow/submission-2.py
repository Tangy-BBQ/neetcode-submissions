class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # looks like dfs or bfs?
        # a kind of path algorithm
        # need to have [0,x] or [x, 0] AND [len(heights[0]), x] or [x, len(heights[0])] in path
        # BFS seems to be the better options here but we only add items with the condition met
        # need to also keep a visited set
        # we can have multiple paths so we need to check all 
        # first we need to get the paths
        # then we need to check if each is valid

        
        # list of sets of paths - we can use this to avoid redundancy
        paths = []
        path_flags = []

        # we create a boolean grid for anything that has been validated already
        # we know a new node is valid if it can reach an existing valid node
        # we should keep two flags here
        valid_grid = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]

        def dfs(x, y, prev_height):
            # check validity first
            if (x, y) in visited:
                return False, False
            if x < 0 or x >= len(heights):
                return False, False
            if y < 0 or y >= len(heights[0]):
                return False, False
            if prev_height < heights[x][y]:
                return False, False
            

            visited.add((x,y))

            if valid_grid[x][y]:
                return True, True

            # setup the valid checks
            valid1 = False
            valid2 = False
            if x == 0 or y == 0:
                valid1 = True
            if x == len(heights)-1 or y == len(heights[0])-1:
                valid2 = True
            # this dfs needs to only visit new nodes
            # it needs to reuse previous findings and flags

            neighbors = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]

            
            for n in neighbors:
                
                # we call our neigbhor to tell update its own flags
                # if any are FULLY valid we know we can return True and update both of our flags
                cur1, cur2 = dfs(n[0], n[1], heights[x][y])
                # but what if only partly valid?
                # we need one from each side to meet here
                valid1 = valid1 or cur1
                valid2 = valid2 or cur2
            if valid1 and valid2:
                valid_grid[i][j] = True
            return valid1, valid2
            

                

                        
        valid = []
        # we are going to check each and then add it to a relevant path based on its neighbors
        # for each path we add we should be keeping track of two flags
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if valid_grid[i][j]:
                    valid.append([i, j])
                    continue
                visited = set()
                cur1, cur2 = dfs(i, j, 1001)
                if cur1 and cur2:
                    # valid = valid + list(visited)
                    valid_grid[i][j] = True
                    valid.append([i, j])

        return valid
        

            