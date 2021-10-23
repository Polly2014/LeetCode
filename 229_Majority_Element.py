# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-22 22:30:00
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-22 22:37:26
from typing import List
from collections import Counter


class Solution:
        # python Counter
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [k for k, v in dict(Counter(nums)).items() if v > len(nums) / 3]

    # 摩尔投票
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        element1, element2 = 0, 0
        vote1, vote2 = 0, 0
        for num in nums:
            if num == element1 and vote1 > 0:
                vote1 += 1
            elif num == element2 and vote2 > 0:
                vote2 += 1
            elif vote1 == 0:
                element1 = num
                vote1 += 1
            elif vote2 == 0:
                element2 = num
                vote2 += 1
            else:
                vote1 -= 1
                vote2 -= 1
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == element1 and vote1 > 0:
                cnt1 += 1
            if num == element2 and vote2 > 0:
                cnt2 += 1
        if vote1 > 0 and cnt1 > len(nums) / 3:
            ans.append(element1)
        if vote2 > 0 and cnt2 > len(nums) / 3:
            ans.append(element2)
        return ans
