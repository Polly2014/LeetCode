# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-31 11:46:03
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-31 12:06:28
from typing import List


class Solution:

    # 大数据超时
    # def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
    #     ans = [0] * n
    #     for first, last, seats in bookings:
    #         for i in range(first - 1, last):
    #             ans[i] += seats
    #     return ans

    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * (n + 1)
        for first, last, seats in bookings:
            ans[first - 1] += seats
            ans[last] -= seats
        for i in range(1, n + 1):
            ans[i] += ans[i - 1]
        return ans[:-1]


if __name__ == '__main__':
    s = Solution()
    print(s.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5))
