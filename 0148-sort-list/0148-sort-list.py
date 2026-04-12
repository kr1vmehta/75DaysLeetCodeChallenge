# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mid(self,head: Optional[ListNode]):
        prev=None
        slow=head
        fast=head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        mi=prev
        return mi
    def sort(self,head: Optional[ListNode]):
        if head==None or head.next==None:
            return head
        m=self.mid(head)
        left=head
        right=m.next
        m.next=None
        left=self.sort(left)
        right=self.sort(right)
        return self.merge(left,right)
    def merge(self, left: Optional[ListNode], right : Optional[ListNode]):
        curr=ListNode()
        dummy=curr
        while left and right:
            if left.val<right.val:
                curr.next=left
                curr=left
                left=left.next
            else:
                curr.next=right
                curr=right
                right=right.next
        while left:
            curr.next=left
            curr=left
            left=left.next
        while right:
            curr.next=right
            curr=right
            right=right.next
        return dummy.next

            






    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.sort(head)

        