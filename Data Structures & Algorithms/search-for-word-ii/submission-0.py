class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # we may think of this as a decision tree of choices
        # we want to find each word present meaning we must find the start end and 
        # all adjacent components in hte middle which are uninteruppted
        # an obvious choice is to perform dfs on letters where we have a match in the list
        # if the first letters match we know what to look for, we can ignore all else
        # so we start with a valid letter and a set of words to seek
        # the main problem is in repeating work
        # we can use dp to store previously explored strings
        # the key is the x,y combo and the value would be a list of words etc
        
        # if we think in terms of bfs we have a target letter and a list of choices
        # we must explore all that are valid for any of our words
        # we may also think of a trie
        # a trie stores the words as a cascading decision of inclusions and stops
        # 'batter' for example has 'bat' ('bat') -> 'ter' ('batter')
        # this will be our main use case for preventing duplicate work
        # we would only be looking at valid components so a trie makes sense

        # so to start we will sort our words

        # brute force is to perform bfs/dfs on all starts searching for the valid potential words
        # can we convert the grid into a trie?


        class TrieNode :
            def __init__(self):
                self.children = {}
                self.word = False

            def add_word(self, word):
                cur = self
                for c in word:
                    if c not in cur.children:
                        cur.children[c] = TrieNode()
                    cur = cur.children[c]
                cur.word = True

        root = TrieNode()
        for w in words:
            root.add_word(w)

        found = set()
        visited = set()

        def dfs(i,j, node, word):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return
            # if no children match the current we fail
            if not board[i][j] in node.children or (i,j) in visited:
                return
            
            # we choose the matching node
            node = node.children[board[i][j]]
            word = word + board[i][j]
            visited.add((i,j))
            if node.word:
                found.add(word)

            # for each direction we try to continue
            dfs(i + 1, j, node, word)
            dfs(i - 1, j, node, word)
            dfs(i, j + 1, node, word)
            dfs(i, j - 1, node, word)
            visited.remove((i,j))



        # we must find all suitable starts
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j, root, "")

        return list(found)
