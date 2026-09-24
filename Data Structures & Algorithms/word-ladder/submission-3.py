class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # this almost seems like an edit distance
        # our answer at MINIMUM would be the edit distance but we have addiitonal
        # constraints to only use the wordList
        # for each words we either choose to switch, choose not to, or it is invalid
        # this gives a decision tree with 3 branches at each word
        # one of which is not an actual choice leaving 2
        # so our real decision tree has branches equal to the number of valid swaps
        # we know we would not want to repeat a word
        # this would create a cycle 
        # we have n! possibilities, can we do better?
        # we cannot assume that getting one letter swapped correctly means it will stay as such
        # we may have the case where we swap 2 correctly at a time then must revert one of them

        # oh we need to have exactly ONE change
        # this makes things a bit easier
        # we would then never change a letter back as it suggests a better path

        # so we just swap one letter at a time
        # we would want to check m options

        adj = {}
        # n 
        for word in [beginWord] + wordList:
            for i in range(len(word)):
                cur = word[:i]+'*'+word[i+1:]
                adj[cur] = adj.get(cur, []) + [word]
        print(adj)


        queue = deque([(beginWord, 1)])
        avail = set(wordList)

        while queue:
            word, l = queue.popleft()
            print(word)
            
            if word == endWord:
                return l
            for i in range(len(word)):
                cur = word[:i]+'*'+word[i+1:]
                for pos in adj[cur]:
                    if pos in avail:
                        queue.append((pos, l + 1))
                        avail.remove(pos)
        return 0

        
                



