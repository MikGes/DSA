#In this solution it also checks for a cycle in any position in the linked list. But the time is terrible so better to follow the next solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        arr = []
        temp = head
        while temp:
            if temp.next not in arr:
                arr.append(temp)
                temp = temp.next
            else: return True
        return False
    #Here is the solution that uses the two-pointer technique to detect a cycle in the linked list. The slow pointer moves one step at a time while the fast pointer moves two steps at a time. If there is a cycle, the fast pointer will eventually meet the slow pointer. If there is no cycle, the fast pointer will reach the end of the list.
  # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s,f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False