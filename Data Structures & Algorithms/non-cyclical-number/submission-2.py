class Solution:
    def isHappy(self, n: int) -> bool:
        # we basically need to use mod to strip each 
        # or make it a string and use type casting

        res = n
        seen = set()
        while res not in seen:
            # print(res)
            cur_res = 0
            for c in str(res):
                cur_res += int(c) * int(c)

            seen.add(res)
            res = cur_res
            
            if res == 1:
                return True
        return False
        


        