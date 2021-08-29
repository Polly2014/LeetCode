# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-29 20:21:45
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-29 21:45:08
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(n):
            left, right = i + 1, n - i
            left_even = int((left + 1) / 2)
            right_even = int((right + 1) / 2)
            left_odd = int(left / 2)
            right_odd = int(right / 2)
            # print('i={}, ans={}'.format(i, (left_even * right_even + left_odd * right_odd) * arr[i]))
            ans += (left_even * right_even + left_odd * right_odd) * arr[i]
        return int(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
