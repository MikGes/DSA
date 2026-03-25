# Here`s a Python implementation of the solution to reverse a linked list between positions left and right:
# We will use a dummy node to handle edge cases where the head of the linked list might be reversed. We will first move the prev pointer to the node just before the left position. Then we will reverse the nodes between left and right by adjusting the next pointers accordingly. Finally, we will return the next pointer of the dummy node as the new head of the linked list.`
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy_node = ListNode(0, head)
        prev = dummy_node
        for _ in range(left - 1):
            prev = prev.next
        current_node = prev.next
        for _ in range(right - left):
            temp = current_node.next         
            current_node.next = temp.next    
            temp.next = prev.next     
            prev.next = temp 
        return dummy_node.next 
