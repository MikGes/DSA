# Here there are two solutions to reverse a linked list. The first one uses an array to store the nodes and then reverses the array to reconstruct the linked list. The second solution uses three pointers (previous, current, next) to reverse the linked list in place without using extra space. The second solution is more efficient in terms of space complexity.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # if head is None:
        #     return head
        # temp = head
        # a = []
        # while temp:
        #     a.append(temp)
        #     temp = temp.next
        # a.reverse()
        # head = a[0]
        # if len(a) == 1:  
        #     head.next = None
        #     return head
        # head.next = a[1]
        # for i in range(1, len(a) - 1):
        #     if a[i+1]:
        #         a[i].next = a[i+1]
        # a[-1].next = None
        # return head
        p = None
        c = head
        while(c != None):
            n = c.next
            c.next = p
            p = c
            c = n
        head = p
        return head