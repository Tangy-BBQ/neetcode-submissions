class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums)-1:
            # we want to contain all things currently available
            # we want to maximize our right pointer while keeping track of our zone
            f = 0
            for i in range(l, r+1):
                f = max(f, i + nums[i])
            
            l = r + 1
            r = f
            res += 1
        return res