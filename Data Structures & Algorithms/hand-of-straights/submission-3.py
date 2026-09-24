class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        

        count = Counter(hand)

        for card in sorted(hand):
            while count[card] > 0:
                # now we need to check the remaining for this potential group

                for i in range(card, card+groupSize):
                    if count[i] == 0:
                        return False
                    count[i] -= 1 

        return True





