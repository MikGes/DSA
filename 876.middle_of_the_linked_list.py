#Here is the solution for the problem "876. Middle of the Linked List" on LeetCode.
#store the nodes in a dictionary and return the middle node based on the length of the dictionary. If the length is even, return the node at index len(d) // 2, otherwise return the node at index (len(d) // 2) + 1.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head.next: return head
        if not head.next.next: return head.next
        d = {}
        c = 0
        temp = head
        while temp.next:
            d[c] = temp
            c += 1
            temp = temp.next
        if len(d) % 2 is 0:
            return d[len(d) // 2]
        return d[(len(d) // 2) + 1]
#Here is another solution that uses the two-pointer technique to find the middle node of the linked list. The slow pointer moves one step at a time while the fast pointer moves two steps at a time. When the fast pointer reaches the end of the list, the slow pointer will be at the middle node.
#class Solution(object):
    # def middleNode(self, head):
    #     """
    #     :type head: Optional[ListNode]
    #     :rtype: Optional[ListNode]
    #     """
    #     slow, fast = head, head
    #     while fast != None and fast.next != None:
    #         slow = slow.next
    #         fast = fast.next.next
    #     return slow
    
    