# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-27 11:17:21
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-27 11:23:09
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    	def reverse_linked_list(head):
    		pre = None
    		cur = head
    		while cur:
    			nxt = cur.next
    			cur.next = pre
    			pre = cur
    			cur = nxt
    	dummy = ListNode(-1)
    	dummy.next = head
    	pre = dummy

    	# 第1步：从虚拟头节点走到left-1步，来到left节点的前一个节点
    	for _ in range(left-1):
    		pre = pre.next

    	# 第2步：从pre再走right-left+1步，来到right节点
    	right_node = pre
    	for _ in range(right-left+1):
    		right_node = right_node.next

    	# 第3步：切断出一个子链表
    	left_node = prev.next
    	curr = right_node.next

    	# 切断链接
    	pre.next = None
    	right_node.next = None

    	# 第4步：反转链表子区间
    	reverse_linked_list(left_node)

    	# 第5步：接回到原来的链表中
    	pre.next = right_node
    	left_node.next = curr
    	return dummy.next