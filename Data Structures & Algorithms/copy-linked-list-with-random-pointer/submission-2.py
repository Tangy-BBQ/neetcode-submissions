"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # creating a copy should be a matter of keeping track of in line nodes for random copy
        # the main issue is that node values may not be unique
        # we are then unable to know which is which
        # we cannot even use the combination of cur, next, random as this may repeat

        # it seems like we may need to traverse both simultaneously?
        # is there a way to store a node in a hash?

        # if we have a node how do we ensure that the two paths are not duplicated 
        # and are instead the exact same objects?

        # if we create the base copy and leave random as blanks we could possibly traverse both?
        # if we know the index in the list of our random we can copy that and then attach
        # we need to be able to hash a node to an index

        if head == None:
            return None
        node_index = {}
        node_from_index = {}
        new_nodes = []
        i = 0
        cur = head
        while cur:
            new_nodes.append(Node(cur.val))
            node_index[cur] = i

            node_from_index[i] = new_nodes[i]

            cur = cur.next
            i += 1

        # now we have our node hash map
        # we can traverse sequentially and randomly to attach each new copy based on the index
        cur = head
        i=0
        while cur:
            # we have our original and need to copy the paths based on index
            next = cur.next
            random = cur.random

            print(cur.val, next.val if next else "", random.val if random else "")

            if next:
                next_i = node_index[next]
            if random:
                random_i = node_index[random]

            # we can now retrieve the NEW nodes for attatching

            new_node = new_nodes[i]
            if next:
                new_node.next = node_from_index[next_i]
            else:
                new_node.next = None
            if random:
                new_node.random = node_from_index[random_i]
            else:
                new_node.random = None

            cur = cur.next
            i += 1

        return new_nodes[0]
            

        