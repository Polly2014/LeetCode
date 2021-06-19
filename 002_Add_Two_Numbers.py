# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-14 22:08:39
# @Last Modified by:   polly
# @Last Modified time: 2021-06-17 22:06:54

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = head = ListNode(0)
        while l1 or l2:
            flag = 0
            if l1:
                curr.val += l1.val
                l1 = l1.next
            if l2:
                curr.val += l2.val
                l2 = l2.next
            flag += curr.val // 10
            curr.next = ListNode(flag)
            curr.val = curr.val % 10
            if l1 or l2 or flag != 0:
                curr = curr.next
            else:
                curr.next = None
        return head

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 首先创建一个虚拟节点，并创建一个current指针，指向这个节点
        current = dummy = ListNode()
        # 初始化carry和两个链表对应节点相加的值
        carry, value = 0, 0
        # 下面的while循环中之所以有carry，是为了处理两个链表最后节点相加出现进位的情况
        # 当两个节点都走完而且最后的运算并没有进位时，就不会进入这个循环
        while carry or l1 or l2:
            # 让value先等于carry既有利于下面两个if语句中两个对应节点值相加，
            # 也是为了要处理两个链表最后节点相加出现进位的情况
            value = carry
            # 只要其中一个链表没走完，就需要计算value的值
            # 如果其中一个链表走完，那么下面的计算就是加总carry和其中一个节点的值
            # 如果两个链表都没走完，那么下面的计算就是carry+对应的两个节点的值
            if l1:
                l1, value = l1.next, l1.val + value
            if l2:
                l2, value = l2.next, l2.val + value
            # 为了防止value值大于十，出现进位，需要特殊处理
            # 如果value小于十，下面这行的操作对于carry和value的值都没有影响
            carry, value = divmod(value, 10)
            # 利用value的值创建一个链表节点，并让current.next指向它
            current.next = ListNode(value)
            # 移动current指针到下一个节点
            current = current.next
        # 最后只要返回dummy的下一个节点就是我们想要的答案。
        return dummy.next
