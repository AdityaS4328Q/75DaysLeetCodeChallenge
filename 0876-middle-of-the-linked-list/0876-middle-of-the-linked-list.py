# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        d.next=head
        slow=fast=d
        while fast and fast.next:
            fast= fast.next.next
            slow= slow.next

            if fast == None:
                return slow
        return slow.next


        # slow = head
        # fast = head
 
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
 
        # return slow