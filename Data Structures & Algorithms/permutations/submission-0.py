class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # this seems like a simple backtracking problem
        # we will add our current to all permutations that we have already found

        # at our base case, we need our path, if set is empty then we add to total

        total = []

        

        def rec(path, n):
            # print(path, n)
            if not n:
                # we have nothing left we can add
                total.append(path.copy())
            
            for cur in list(n):
                # print(n, cur)
                path.append(cur)
                n.remove(cur)
                rec(path, n)
                path.pop()
                n.add(cur)
        
        rec([], set(nums))
        return total

        