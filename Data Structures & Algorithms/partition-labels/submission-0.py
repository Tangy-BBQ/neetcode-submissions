class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # maximize the number of substrings
        # BUT letters can only be used in one substring
        # we also need the lengths of the substrings

        # we know that everything within two matching chars MUST all be in one string
        # we can identify each string and its required matches
        # for each letter we will create a set of matches and expand out to encompass all
        # this would be n*m where m in the number of unique letters (constant?)

        # i think since we only have 27 letter we can assume m is irrelevant
        # if we used integers we would be n*m

        # if we map the first and last occurence of each letter we could construct the overlap
        # maybe for each index 

        chars = {}

        for i in range(len(s)):
            cur = chars.get(s[i], [None, None])
            if cur[0] == None:
                cur[0] = i
            if cur[1] == None or cur[1] < i:
                cur[1] = i
            chars[s[i]] = cur

        print(chars)

        # need to check what is currently open and find everything that is joined even indirectly
        # we can check if i is within any starts
        cur_open = set()
        cur_start = -1
        lens = []
        for i in range(len(s)):
            
            for key, (start, end) in chars.items():
                if i == start:
                    cur_open.add(key)
                if i == end and key in cur_open:
                    cur_open.remove(key)
            
            
              
            print(cur_open)
            if len(cur_open) == 0:
                lens.append(i-cur_start)
                cur_start = i
            
        return lens