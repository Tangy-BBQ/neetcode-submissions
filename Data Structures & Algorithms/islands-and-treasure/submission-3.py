class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 0:
                    q.append([x, y])
                    visited.add((x, y))
        
        dist = 0

        while q:
            for i in range(len(q)):
                x, y = q.popleft()

                grid[x][y] = dist

                for k in [-1, 1]:
                    if x + k >= 0 and x + k < len(grid) and (x + k, y) not in visited and grid[x + k][y] != -1:
                        q.append([x + k, y])
                        visited.add((x + k, y))
                    if y + k >= 0 and y + k < len(grid[x]) and (x, y + k) not in visited and grid[x][y + k] != -1:
                        q.append([x, y + k])
                        visited.add((x, y + k))
            dist += 1

                

                            
            

