class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # ok we want to find a MIN for k
        # our easiest bay to eat all the bananas is to simply eat the max of any pile
        # BUT since we want to minimize with only h as our constraint we need to be strategic

        # since we are looking for our minimum we could brute force by starting at k=1
        # we then compute how long it takes and return as soon as we are within h

        # this will be slow as we have O(piles * k)

        # if we can somehow use the factors of our piles
        # we basically need the least factor for h/len(piles) to fit into the size of the largest pile

        # factor1 = math.ceil(h/len(piles))
        max_speed = max(piles)

        l = 1
        r = max_speed

        while l <= r:
            center = (l+r)//2

            total = 0
            for p in piles:
                total += math.ceil(float(p)/center)
            if total <= h:
                max_speed = center
                r = center - 1
            else:
                l = center + 1
        return max_speed
            
