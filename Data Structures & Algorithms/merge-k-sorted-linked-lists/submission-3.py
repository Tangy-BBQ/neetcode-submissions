# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # if we can merge two lists, we can merge k
        # we will just keep merging the new list with the next one
        # we require 2+ lists for this
        # O(n*k)
        print(lists)
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        # now we keep merging the two lists

        head_list = lists.pop()
        dummy = ListNode("dummy", head_list)
        while lists:
            # next_list = lists.pop()
            # merge the current two lists
            # we need to keep track of BOTH lists and iterate in parallel to maintain O(n)

            # we also need a prev pointer OR a dummy head
            # we should start at the beginning EACH TIME
            cur_prev = dummy
            cur_head = dummy.next
            cur_next = lists.pop()

            while cur_next:
                # print(dummy.val, dummy.next.val)
                # print(cur_head.val, cur_next.val)
                # we either are less, equal, or more

                if not cur_head:
                    cur_prev.next = cur_next
                    break
                elif cur_next.val <= cur_head.val:
                    # if we are less than the current we append now
                    # insert here before head list
                    tmp = cur_next
                    cur_next = cur_next.next

                    cur_prev.next = tmp
                    tmp.next = cur_head
                    cur_prev = tmp
                else:
                    cur_prev = cur_head
                    cur_head = cur_head.next
                    
        return dummy.next


        