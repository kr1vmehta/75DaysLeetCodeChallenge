# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=list1
        curr2=list2
        prev=ListNode(-1)
        head=prev
        next_node=None
        while curr1 and curr2:
            if curr1.val < curr2.val:
                prev.next=curr1
                
                next_node=curr1.next
                prev=curr1
                curr1=next_node
            else:
                prev.next=curr2
                next_node=curr2.next
                prev=curr2
                curr2=next_node
        while curr1:
            prev.next=curr1
                
            next_node=curr1.next
            prev=curr1
            curr1=next_node
        while curr2:
            prev.next=curr2
            next_node=curr2.next
            prev=curr2
            curr2=next_node
        head=head.next
        return head
        

        