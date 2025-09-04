# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next =None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1:ListNode, list2:ListNode):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        merged = ListNode()
        
        merged = list1
        
        while list1 is not None:
            list1 = list1.next
        
        
        return merged
        
node3 = ListNode(4)
node2 = ListNode(2,node3)        
node1 = ListNode(1,node2)
        
        
node6 = ListNode(4)
node5 = ListNode(3,node6)        
node4 = ListNode(1,node5)

s = Solution
s.mergeTwoLists(node1,node4)
        