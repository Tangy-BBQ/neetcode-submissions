class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # the main question is if we should tackle each individually
        # or if there is a best order?
        # if we check each individually we have (9*9) * (9 + 9 + 9)
        # if anything fails we fail immediately
        # if we get to the end we pass

        # we can save time by computing each box and each row only once
        # this would be visiting everything without extra operations

        for row in range(len(board)):
            # keep track of the current
            # if we see any duplicates we fail
            count = {}
            for col in range(len(board[0])):
                count[board[row][col]] = count.get(board[row][col], 0) + 1
            # check if any extras
            for k, v in count.items():
                if k != '.' and v > 1:
                    return False
        
        # we probably could do this in one pass but for simplicity we start with 2
        for col in range(len(board[0])):
            # keep track of the current
            # if we see any duplicates we fail
            count = {}
            for row in range(len(board)):
                count[board[row][col]] = count.get(board[row][col], 0) + 1
            # check if any extras
            for k, v in count.items():
                if k != '.' and v > 1:
                    return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                # we need to check each of the 9 sub squares

                # i and j will be our top left for the current

                count = {}
                for k in range(3):
                    for l in range(3):
                        # this is our current small box
                        count[board[i+k][j+l]] = count.get(board[i+k][j+l], 0) + 1
                # is this O(n^3)?
                for k, v in count.items():
                    if k != '.' and v > 1:
                        return False
        return True



