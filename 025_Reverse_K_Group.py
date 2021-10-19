# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-17 23:59:23
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-18 00:05:31
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
        # 栈
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        while True:
            count = k
            stack = []
            tmp = head
            # 往后读k个节点
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            # 当count不为0说明不够长
            if count:
                p.next = head
                break
            # 够长，则开始反转
            while stack:
                p.next = stack.pop()
                p = p.next
            # 与剩下的连起来
            p.next = tmp
            head = tmp
        return dummy.next


    # 递归
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1
            head = cur
        return head
