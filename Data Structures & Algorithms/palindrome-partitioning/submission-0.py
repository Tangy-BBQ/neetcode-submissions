class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # we have to look at two components
        # the current USED palindromes and the unsued remainder
        # our base case it to use all single chars
        
        # if we are looking at a string s and have all combos for [i+1:len(s)]
        # all we need to know is if s[i:len(s)] is a palindrome and we also simply add s[i]

        dp = [[] for _ in range(len(s) + 1)]
        dp[len(s)] = [[]]

        is_pal = [[False] * len(s) for _ in range(len(s))]


        for i in range(len(s)-1, -1, -1):
            # we always add s[i]
            # need to check if s[i:len(s)] is valid
            for j in range(i+1, len(s)+1):
                # check if our contained substring is a palindrome
                if s[i] == s[j - 1] and (j - 1 - i < 2 or is_pal[i + 1][j - 2]):
                        is_pal[i][j - 1] = True
                        
                        candidate = s[i:j]
                        for part in dp[j]:
                            dp[i].append([candidate] + part)
        return dp[0]
                


        
            

