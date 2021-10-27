# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-26 22:52:32
# @Last Modified by:   polly
# @Last Modified time: 2021-10-27 20:19:10
from typing import List


class Solution:
	# 单调栈
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map_greater = {}
        stack = []
        for num in reversed(nums2):
            while stack and num > stack[-1]:
                stack.pop()
            map_greater[num] = stack[-1] if stack else -1
            stack.append(num)
        return [map_greater[num] for num in nums1]
