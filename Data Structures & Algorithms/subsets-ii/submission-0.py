class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # so we want all new subsets but our list has duplicates
        # we want to avoid running the same thing twice
        # we could create a counter of each
        # then we would 

        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        print(count)
        # now we use our counts to do the following
        # we either add the current and subtract whats available
        # OR we skip the add and pass it along to be added later

        res = [[]]

        for k, v in count.items():
            tmp = res.copy()
            new_vals = []
            for t in tmp:
                for i in range(v+1):
                    #
                    new_vals.append(t + [k]*i)
            res = new_vals
        return res



                
            