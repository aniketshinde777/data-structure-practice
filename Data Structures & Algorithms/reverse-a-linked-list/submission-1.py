# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:
            next_node = curr.next #1
            curr.next = prev #pointing to reverse i.e 1 -> None next iteration 2 -> 1 -> None
            prev = curr # updating prev  
            curr = next_node # updating curr to next Node
        return prev





"""
1 -> 2 -> 3 ->4

curr = 2 -> 3 -> 4
prev = 1 -> prev

"""

    
       
