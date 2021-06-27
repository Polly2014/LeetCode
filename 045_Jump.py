# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-06-27 17:55:34
# @Last Modified by:   Polly
# @Last Modified time: 2021-06-27 18:50:54
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        # dp_min_jump[i]: 到达数组长度为i的最后位置的最少条约次数
        n = len(nums)
        dp_min_jump = [n + 1] * n
        dp_min_jump[0] = 0
        for i in range(1, n):
            # 第i个位置，需要考虑i之前所有的元素0<=j<i
            #   如何第j个元素上的值加上j大于等于i，那么dp_min_jump[i]就是dp_min_jump[j]+1的最小值
            for j in range(i):
                if j + nums[j] >= i:
                    dp_min_jump[i] = min(dp_min_jump[i], dp_min_jump[j] + 1)
        return dp_min_jump[n - 1]
        '''
        n = len(nums)
        dp_min_jump = [n + 1] * n
        dp_min_jump[0] = 0
        for i in range(n - 1):
            end = min(n, i + nums[i] + 1)
            for j in range(i + 1, end):
                dp_min_jump[j] = min(dp_min_jump[j], dp_min_jump[i] + 1)
        return dp_min_jump[n - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))
