class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        pretot = 1
        posttot = 1

        for i in range(len(nums)):
            prefix[i] = pretot * nums[i]
            pretot = prefix[i]
            postfix[len(nums) - i - 1] = posttot * nums[len(nums) - i - 1]
            posttot = postfix[len(nums) - i - 1]
        # print(prefix, postfix)
        for i in range(len(nums)):
            if i == 0:
                nums[i] = postfix[i + 1]
            elif i == len(nums) - 1:
                nums[i] = prefix[i - 1]
            else:
                nums[i] = prefix[i - 1] * postfix[i + 1]

        return nums
        