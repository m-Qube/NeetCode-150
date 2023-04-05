class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr, prev = head, None
        # Time - O(N) & Space - O(1)
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
    
        return prev
