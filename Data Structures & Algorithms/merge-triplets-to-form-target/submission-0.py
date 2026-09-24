class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # brute force: look through all pairs and find the max of each element
        # return true only if the condition is met
        # how to be faster? the target is only valid if we have the numbers present
        # we can skip anything with a number higher for a given index
        # in one pass we could keep track of possible pairs and eliminate anything
        # we also require at least 1 match
        # this however does not decrease the complexity

        valid = []

        for i in range(len(triplets)):
            invalid = False
            any_match = False
            for j in range(3):
                if triplets[i][j] > target[j]:
                    invalid = True
                if triplets[i][j] == target[j]:
                    any_match = True
            if not invalid and any_match:
                valid.append(triplets[i])
        a = b = c = False
        for i in range(len(valid)):
            if valid[i][0] == target[0]:
                a = True
            if valid[i][1] == target[1]:
                b = True
            if valid[i][2] == target[2]:
                c = True

        if a and b and c:
            return True
        return False

