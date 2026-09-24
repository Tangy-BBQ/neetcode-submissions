class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # simple: sort and go through linearly O(nlogn)
        # need O(n) solution
        # nums[i] can be positive or negative, cant create inclusion array
        # create set from nums, go through nums linearly and check each index for prev and next vals in the set

        nset = set(nums)
        lcs = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in nset:
                # start of a seq
                length = 1
                cur = nums[i]
                while cur + 1 in nset:
                    length += 1
                    cur = cur + 1
                lcs = max(lcs, length)
        
        return lcs

                
                

