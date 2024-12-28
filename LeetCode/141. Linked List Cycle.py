# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
    

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         visited = set()

#         current = head
#         while current:
#             if current in visited:
#                 return True  # Cycle detected
#             visited.add(current)
#             current = current.next

#         return False  # No cycle detected
