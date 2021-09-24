# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-24 20:51:54
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-24 21:05:41


# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
        # 递归
    def flatten(self, head: 'Node') -> 'Node':
        dummy = Node(0)
        dummy.next = head
        while head:
            if head.child == None:
                head = head.next
            else:
                tmp = head.next
                chead = self.flatten(head.child)
                head.next = chead
                chead.prev = head
                head.child = None
                while head.next:
                    head = head.next
                head.next = tmp
                if tmp:
                    tmp.prev = head
                head = tmp
        return dummy.next


if __name__ == '__main__':
        # s = Solution()
        # s.flatten(head: 'Node')
    dummy = Node(0)
