class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # this will basically be bfs or dfs
        # we need to prevent revisiting nodes
        # we will have O(n*m)

        # the main issue is being inplace as we need to 
        # maintain all things that are visited and then update

        def dfs(x, y, visited):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return False
            if (x, y) in visited or board[x][y] == 'X':
                return False
            visited.add((x, y))
            # we need to know if we are X or O
            # if we are an X we can skip
            # if we are an O we must know if we can exit or not

            # first we must visit all nodes and add them to our set
            # this result is useful for making updates in case we are isolated
            res1 = dfs(x + 1, y, visited)
            res2 = dfs(x - 1, y, visited)
            res3 = dfs(x, y + 1, visited)
            res4 = dfs(x, y - 1, visited)
            res = res1 or res2 or res3 or res4
            
            # we can exit if we can touch an edge
            if x == 0 or x + 1 == len(board) or y == 0 or y + 1 == len(board[0]):
                return True
            return res

        to_visit = {(r, c) for r in range(len(board)) for c in range(len(board[0]))}

        while to_visit:
            visited = set()
            x, y = to_visit.pop()
            if not dfs(x, y, visited):
                # we need to update all in visited
                for point in visited:
                    # print(point)
                    board[point[0]][point[1]] = 'X'

        return
            

        