# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -=1
        
        while right:
            left = left.next
            right = right.next
    
        left.next = left.next.next
        return dummy.next


        

"""
1 2 3 4    2 
1 -> 2 -> 3 -> 4

2.next -> 3.next
3.next -> None


challenges
    -> how to know which element to remove
        -> 
    -> how to store the prev element
        -> for this we can have a prev var which would track


"""
        