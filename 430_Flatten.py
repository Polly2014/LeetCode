# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-24 20:51:54
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-24 23:10:44


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

    # 递归优化
    def flatten(self, head: 'Node') -> 'Node':
        def DFS(head):
            last = head
            while head:
                if head.child == None:
                    last = head
                    head = head.next
                else:
                    tmp = head.next
                    childLast = DFS(head.child)
                    head.next = head.child
                    head.child.prev = head
                    head.child = None
                    if childLast:
                        childLast.next = tmp
                    if tmp:
                        tmp.prev = childLast
                    last = head
                    head = childLast
            return last
        DFS(head)
        return head

    # 迭代
    def flatten(self, head: 'Node') -> 'Node':
        cur = head
        while cur:
            # 遇到包含child的节点
            if cur.child:
                # 断开原链表
                nxt = cur.next
                child = cur.child
                cur.next = child
                cur.child = None
                # 重新拼接
                child.prev = cur
                while child.next:
                    child = child.next
                child.next = nxt
                if nxt:
                    nxt.prev = child
            cur = cur.next
        return head


if __name__ == '__main__':
        # s = Solution()
        # s.flatten(head: 'Node')
    dummy = Node(0)
