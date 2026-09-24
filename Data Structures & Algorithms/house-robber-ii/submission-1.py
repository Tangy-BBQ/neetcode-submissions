class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        prev1a = nums[0]
        prev2a = nums[0]

        prev1b = nums[1]
        prev2b = 0

        for i in range(2, len(nums)):

            if i + 1 < len(nums):
                temp = max(prev1a, prev2a + nums[i])
                prev2a = prev1a
                prev1a = temp

            temp = max(prev1b, prev2b + nums[i])
            prev2b = prev1b
            prev1b = temp
        return max(prev1a, prev1b)