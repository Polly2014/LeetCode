# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-04 22:11:58
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-04 22:28:05
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while slow and fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return
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
