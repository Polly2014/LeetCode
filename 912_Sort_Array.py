# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-07-18 17:36:03
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-06 11:53:19

from typing import List
import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = random.randint(0, len(nums) - 1)
        flag = nums[mid]
        left = list(filter(lambda x: x <= flag, nums[0:mid] + nums[mid + 1:]))
        right = list(filter(lambda x: x > flag, nums[0:mid] + nums[mid + 1:]))
        return self.sortArray(left) + [flag] + self.sortArray(right)


if __name__ == '__main__':
    # s = Solution()
    # print(s.sortArray([1, 2, 5, 9, 3, 6]))
    num = 7
    for i in range(10):
        print(num << i)
    # print(bin(7))
