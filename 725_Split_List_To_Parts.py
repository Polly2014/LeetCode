# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-22 23:36:22
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-23 17:35:55
from typing import List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return 'ListNode({})'.format(self.val)


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        cnt = 0
        curr = head
        # 获取链表长度
        while curr:
            curr = curr.next
            cnt += 1

        # 计算每组的平均长度，以及可以+1的组个数
        num_per_group = cnt // k
        num_plus_one = cnt % k

        ans = [None] * k
        curr = head
        for i in range(k):
            if not curr:
                break
            ans[i] = curr
            # print('i={}, ans={}.'.format(i, ans))
            num_size = num_per_group + (1 if i < num_plus_one else 0)
            # print('i={}, size={}'.format(i, num_size))
            for j in range(1, num_size):
                curr = curr.next
            p_next = curr.next
            curr.next = None
            curr = p_next

        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    i = 0
    curr = head = ListNode(0)
    while i < len(nums):
        curr.next = ListNode(nums[i])
        curr = curr.next
        i += 1
    curr.next = None

    s = Solution()
    print(s.splitListToParts(head.next, 5))
