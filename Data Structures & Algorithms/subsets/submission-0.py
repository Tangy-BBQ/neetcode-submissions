class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # we can iteratively build the sets using a base case and recursive calls
        # we want to add an element each call KNOWING that we are build a new set

        def rec(n):
            # print(n)
            if n == []:
                return [[]]

            # we simply hand off the tail and only worry about adding the current
            # we just need to append it to each list and keep the original
            head = n[0]
            tail = n[1:]
            # print(head, tail)
            res = rec(tail)
            new = []
            for l in res:
                # print(l)
                new.append([head] + l)
            # print(new)
            return res + new
        return rec(nums)