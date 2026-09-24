class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initial idea is to create a frequency map
        # then we sort the keys based on the values
        # this would be O(nlogn)
        # can we do better though?
        # we could do O(n*k) if we iterate to select the incremental top k
        # this is n^2 beause n >= k

        # how to get to linear time?
        # if we had a map then of values to keys we could count our max and continue
        # to decrease and add to a list
        # once we fill our list we return

        # since we are always unique we dont need to worry about conflicts
        # this would still rely on soring in a sense
        # we could have 1000 of the first and only 1 of the second at k=2
        # this would be very slow and still tied to n but thats ok since its just once

        n_count = {}
        # count_n = {}
        count_n = [[] for i in range((len(nums) + 1))]
        

        for n in nums:
            n_count[n] = n_count.get(n, 0) + 1

        for key, val in n_count.items():
            count_n[val].append(key)
       
        # print(count_n)
        res = []
        for i in range(len(count_n) - 1, 0, -1):
            for v in count_n[i]:
                res.append(v)
                if len(res) == k:
                    return res
        return res

        
        