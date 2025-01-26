"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        mapping = {}
        current = head

        while current:
            mapping[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            if current.next:
                mapping[current].next = mapping[current.next]
            if current.random:
                mapping[current].random = mapping[current.random]
            current = current.next

        return mapping[head]



# """
# # Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
# """

# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         if not head:
#             return None

#         current = head
#         while current:
#             new_node = Node(current.val)
#             new_node.next = current.next
#             current.next = new_node
#             current = new_node.next

#         current = head
#         while current:
#             if current.random:
#                 current.next.random = current.random.next
#             current = current.next.next

#         original = head
#         copy = head.next
#         copy_head = copy

#         while original:
#             original.next = original.next.next
#             if copy.next:
#                 copy.next = copy.next.next
#             original = original.next
#             copy = copy.next

#         return copy_head