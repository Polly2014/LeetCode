# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-04 22:11:58
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-04 22:40:02
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = head
                step = 0
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return fast
        return


if __name__ == '__main__':
    head = ListNode(1)
    s = Solution()
    print(s.detectCycle(head))
