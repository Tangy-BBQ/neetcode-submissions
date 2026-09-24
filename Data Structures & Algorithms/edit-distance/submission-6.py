class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # we need to keep track of how we insert delete or replace
        # if we insert we maintain our index (subtract)
        # delete we add
        # if we replace we maintain
        
        # if our current letter matches we can always keep it
        
        # otherwise we must use an operation

        # initial impression is to have two pointer
        # we need to know if we can preserve later portions rather than making an insertion
        # this may be redundant?

        # if we loop we may need to use a while loop to check both
        # if we use recursion we can simply take the minimum of the 3 options

        # how to make faster?
        # we only make modifications to word1 so we can keep a map of modifications for reuse
        # if we see something new we can immediately return the previous computation
        # we can add to mod map when?
        # at our base case and after each iterative version

        mod_map = {}

        def rec(cur1, cur2):
            if (cur1, cur2) in mod_map:
                return mod_map[(cur1, cur2)]
            # our base case is when we run out
            # we need to insert/delete the max of the remaining
            if cur1 == len(word1) or cur2 == len(word2):
                return max(len(word1)-cur1, len(word2)-cur2)
            # head1 = cur1[0]
            # head2 = cur2[0]
            # tail1 = cur1[1:]
            # tail2 = cur2[1:]

            # if equal we advance both and return that recursion
            if word1[cur1] == word2[cur2]:
                return rec(cur1+1, cur2+1)
            # otherwise we need to check if we swap, insert or delete
            swap = mod_map.get((cur1+1, cur2+1), None)
            if not swap:
                swap = rec(cur1+1, cur2+1)
            
            insert = mod_map.get((cur1, cur2+1), None)
            if not insert:
                insert = rec(cur1, cur2+1)
            delete = mod_map.get((cur1+1, cur2), None)
            if not delete:
                delete = rec(cur1+1, cur2)

            # min(swap, insert, delete) + 1
            if swap <= insert and swap <= delete:
                mod_map[(cur1, cur2)] = swap + 1
                return swap + 1
            elif insert <= swap and insert <= delete:
                mod_map[(cur1, cur2)] = insert + 1
                return insert + 1
            elif delete <= swap and delete <= insert:
                mod_map[(cur1, cur2)] = delete + 1
                return delete + 1
        
        return rec(0, 0)


        