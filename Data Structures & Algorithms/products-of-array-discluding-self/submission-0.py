class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total = 1
        zeros = 0
        for i in nums:
            if i == 0:
                zeros = zeros + 1
            else:
                total = total * i
        # print(total)
        if zeros == 1:
            
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] = 0
                else:
                    # print(nums[i], total)
                    nums[i] = total
        elif zeros == 0:
            for i in range(len(nums)):
                nums[i] = int(total / nums[i])
        else:
            return [0] * len(nums)

        return nums
        