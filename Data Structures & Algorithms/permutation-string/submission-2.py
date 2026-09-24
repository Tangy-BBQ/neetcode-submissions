class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # initial idea is simply to make a map of the number of characters for each
        # then we iterate through s2 to check if we reach our requirement
        # we need to use a sliding window to increase our current substring without adding extra chars

        s1_map_orig = {}

        for s in s1:
            s1_map_orig[s] = s1_map_orig.get(s, 0) + 1
        # print(s1_map_orig)

        start = 0

        # we loop until our min length
        while start <= len(s2) - len(s1):
            # every time we increase start we reset s1_map
            s1_map = dict(s1_map_orig)
            end = start
            

            # for each additional char we subtract it from our quota
            while end < len(s2) and s2[end] in s1_map.keys():
                # we only want to increase if our 
                # print(s2[start:end+1])
                cur = s1_map[s2[end]]
                if cur > 0:
                    # we can add it
                    s1_map[s2[end]] = cur - 1
                    end += 1
                else:
                    # we cant and we backup
                    # end -= 1
                    break
                
            # check if our condition is met
            # print(s1_map)
            cond = True
            for key, value in s1_map.items():
                if value != 0:
                    # false and must continue
                    cond = False
                    break
            if cond:
                return True
            start += 1

        return False