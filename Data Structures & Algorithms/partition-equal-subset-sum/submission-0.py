class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # we need ALL elements to be preserved in two distinct subsets whose sums are equal
        # this seems somewhat similar to house robber - we either keep or discard each item
        # we can then have to add discards to our second set
        # the key is index, value is going to be our sum
        # the problem is that we are not maximizing

        # each decision will be 0 (set 1) or 1 (set 2)
        # for the next decision we should check what?

        # we can also look at it as a reductive total
        # we have our total and then decide if we want to subtract and then add to the other
        
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)):
            add = set()
            for j in dp:
                add.add(j + nums[i])
            dp = dp | add
        return target in dp