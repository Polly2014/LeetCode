# -*- coding: utf-8 -*-
# @Author: polly
# @Date:   2021-06-14 21:45:59
# @Last Modified by:   polly
# @Last Modified time: 2021-06-14 21:55:44

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for idx, num in enumerate(nums):
            another = target - num
            flag = ans.get(another)
            if flag != None:
                return [ans[another], idx]
            else:
                ans[num] = idx
