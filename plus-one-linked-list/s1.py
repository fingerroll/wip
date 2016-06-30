class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # node1->node2-> node3
        def reverse(head):
            node = head
            pre = None
            while node:
                tmp = node.next
                node.next = pre
                pre = node
                node = tmp
            return pre
        
        head = reverse(head)
        node = head
        carry = 1
        pre = None
        while carry > 0 and node:
            v = node.val + carry
            node.val = v % 10
            carry = v/10
            pre = node
            node = node.next
        
        if carry > 0:
            pre.next = ListNode(carry)
        
        head = reverse(head)
        return head
        
