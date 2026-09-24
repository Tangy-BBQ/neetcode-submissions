class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if we go sequentially we have O(n)
        # if we had an ordinary sorted list we could binary search in O(logn)
        # we can still apply this with a few catches
        # our main issue is in finding the pivot point
        # once we see WHERE our pivot is we can know when to switch halves
        # we cannot simply check the start as it may start from 1 or 0

        # our pivot is at i where nums[i] > nums[i+1]
        # we must check both directions HOWEVER this is ok if we store the center

        def search_pivot(lower, upper):
            res = -1
            # print(lower, upper)
            if lower == upper:
                return lower - 1
            # we are on the correct path
            if nums[lower] > nums[upper]:
                if lower + 1 == upper:
                    # print("found", lower)
                    return lower
                # check only one side
                center = (lower+upper)//2
                if nums[center] > nums[lower]:
                    res = search_pivot(center, upper)
                else:
                    res = search_pivot(lower, center)
            return res

        pivot = search_pivot(0, len(nums)-1)
        # print(pivot)

        fixed = nums[pivot+1:len(nums)+1] + nums[0:pivot+1]
        # print(fixed)
        # return fixed[0]
        return nums[pivot+1]
