class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # this is a modified type of sort
        # seems similar to insertion sort in some ways

        # we are not guaranteed that we have any valid groups
        # should we sort first?
        # the main problem I see is that if we try to create a group which is incomplete
        # we may need to reuse some later if we dont

        # if we start with a random first number, we need to identify if we have anything before or after it
        # later in the list
        # if we have both we can use both, if only one then we only look in that direction
        # it may be useful to have a map of counts

        # if we have a map of counts we can just check the keys for anything before and after for remaining counts
        # if we are working on a path and find it is invalid we must reset
        # HOWEVER if we ever need to reset we already know we can return False

        hand_map = {}

        for card in hand:
            hand_map[card] = hand_map.get(card, 0) + 1

        # for the second pass we will try to get each card in a group
        # if a group is incomplete we return false early
        # if we have card leftover we also return false

        

        # we need a method of iterating through
        # we will start with the min and then pick a new card that remain after each group completes
        # we always want to have our key as the current min and expand to the right
        key = min(hand) #hand_map[]
        while key != -1:
            # print(hand_map)
            # print(key)
            hand_map[key] = hand_map.get(key, 0) - 1
            curl = key + 1
            
            # curr = key + 1
            cur_group = 1
            # expand to the right until we meet our size
            while cur_group < groupSize:
                next = hand_map.get(curl, None)
                # print(curl)
                # prev = hand_map.get(curr, None)

                # if not next and not prev:
                #     return False

                if next and next > 0:
                    # if hand_map[curl] == 0:

                    hand_map[curl] = hand_map.get(curl, 0) - 1
                    cur_group += 1
                    curl += 1
                else: 
                    # print("HERE")
                    return False
                # if prev > 0:
                #     cur_group += 1
                #     curr += 1

            # now we have met our first group
            # we need to advance to the next group
            # we should find the next lowest card that has count above zero
            
            m = -1
            # can we do anything other than loop?
            for k, v in hand_map.items():
                if v <= 0:
                    continue
                if m == -1 or k < m:
                    m = k
            key = m
        
        for k, v in hand_map.items():
            if v < 0:
                return False
        return True






