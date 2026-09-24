class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # each row and column has a queen
        # when we place a queen we can block out that col row and diag
        # of the remaining spaces we can choose to place another
        # if we reach a point where we cannot place another legally we break
        # this seems like a bit of a stack or rec problem
        # we need to check all possibilities without repeating
        # unless a trick?

        # if we call the recursive start on each x,y we can find our answer
        # can we use symmetry here, we know an invalid x,y start is invalid any rotation
        # we only need the first

        # we would need to be able to update this by both pushing and popping queens
        # while showing the valid pieces
        # we could use a counter? for each invalidation we subtract one more
        # this allows us to keep popping
        
        valid_qs = []

        # if we find a valid queen we return it
        # since we are finding many we return it in a list with the current path
        # the problem is that we may find that two paths are valid
        # we need to return all possible VALID current combinations
        # a list of lists of lists

        # we instead can keep track of our current path and just add it to our valid qs
        def rec(x, y, row, col, diag, path):
            # print(x,y)
            # print(col)
            # print(diag)

            # this is our base case
            # we should only reach this if we are valid
            # PROBLEM we need to start off row and cols
            path = path.copy()
            col = col.copy()
            diag = diag.copy()
            
            # row.append(x)
            path.append((x,y))
            col.append(y)
            count = 0
            for h in range(1, n-x):
                if x + h < n and y + h < n:
                    diag.append((x + h, y + h))
                    count += 1
                if x + h < n and y - h >= 0:
                    diag.append((x + h, y - h))
                    count += 1
            # print(diag)
            if len(col) == n:
                # print(path)
                valid_qs.append(path.copy())
                return
            if x >= n:
                valid_qs.append(path)
                return #[]
            # now we must pick a VALID remaining space on x+1
            # all_paths = [[]]
            # if x + 1 >= n:
            #     # base case - we found a valid solution
            #     all_paths = [[[x,y]]]
            # else:
            # options = []
            # otherwise we keep descending
            # print("huh")
            for i in range(n):
                if i not in col and (x+1, i) not in diag:
                    path.append((x+1, i))
                    qs = rec(x+1, i, row, col, diag, path)
                    path.pop()
                    # print(qs)
                    # we only keep FULL depths
                    
                    # for q in qs:
                    #     print(q, len(q), n-x-1)
                    #     if len(q) == n - x:
                    #         options.append(q)
            # for o in options:
            #     all_paths.append([[x,y]] + [o])
            # row.pop()
            col.pop()
            for _ in range(count):
                diag.pop()
            # print(all_paths)
            return #all_paths

        for i in range(n):
            rec(0, i, [], [], [], [])
            # qs = rec(0, i, [], [], [])
            # print("\n\n")
            # print(qs)
            # print("\n\n")
            # for q in qs:

            #     if len(qs) == n:
            #         valid_qs.append(q)
            # row = [i]
            # col = [col]

            # diag = []#? this will be a set of coordinates
            # diag increase out in 4 direction with a max of n each
            # this is O(n)
            # we can skip rows and columns already used
            # if we are descending by row we never look up only down
        print(valid_qs)

        results = []
    
        for qs in valid_qs:
            base = ['.'*n for _ in range(n)]
            for q in qs:
                # print(q)
                # print(base[q[0]])
                line = list(base[q[0]])
                line[q[1]] = 'Q'
                # print(line)
                base[q[0]] = ''.join(line)
            results.append(base)
        # print(results)
        return results
