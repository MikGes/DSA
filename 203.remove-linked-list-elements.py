#So here we are given the head of a linked list and a value, and we need to remove all the nodes of the linked list that has Node.val == value, and return the new head.
#We can use the concept of a dummy node to handle edge cases where the head node itself needs to be removed. We will iterate through the linked list and check if the next node's value is equal to the given value. If it is, we will skip that node by changing the next pointer of the current node. If it is not, we will move to the next node. Finally, we will return the next pointer of the dummy node as the new head of the linked list.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy_node = ListNode(-1)
        dummy_node.next = head
        current_node = dummy_node
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return dummy_node.next