# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-07 17:57:29
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-07 20:02:15
from typing import List
from queue import Queue


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i]:
                sign = nums[i] > 0
                visited = set()
                current = nums[i]
                while i not in visited:
                    if current == 0 or (current > 0) != sign:
                        break
                    if current % n == 0:
                        break
                    visited.add(i)
                    current = nums[(i := (i + current + n) % n)]
                else:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.circularArrayLoop([2, -1, 1, 2, 2]))
