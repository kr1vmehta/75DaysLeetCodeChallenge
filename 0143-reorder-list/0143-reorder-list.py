# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head: Optional[ListNode]):
        prev=None
        next_node=None
        curr=head
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        mid=slow.next
        slow.next=None
        l2=self.reverse(mid)
        curr1=head
        curr2=l2
        while curr1 and curr2:
            next_1=curr1.next
            if curr2:
                next_2=curr2.next
            curr1.next=curr2
            curr2.next=next_1
            curr1=next_1
            curr2=next_2
        return head