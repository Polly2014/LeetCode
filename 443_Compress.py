# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-21 14:14:31
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-21 16:00:04
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        r_l, w = 0, 0
        for r_r in range(n):
            if r_r == n - 1 or chars[r_r] != chars[r_r + 1]:
                chars[w] = chars[r_r]
                w += 1
                cnt = r_r - r_l + 1
                if cnt > 1:
                    cnt = list(str(cnt))
                    for i in range(len(cnt)):
                        chars[w] = cnt[i]
                        w = w + 1
                r_l = r_r + 1
        return w

    # def compress(self, chars: List[str]) -> int:
    #     def reverse(left: int, right: int) -> None:
    #         while left < right:
    #             chars[left], chars[right] = chars[right], chars[left]
    #             left += 1
    #             right -= 1

    #     n = len(chars)
    #     write = left = 0
    #     for read in range(n):
    #         if read == n - 1 or chars[read] != chars[read + 1]:
    #             chars[write] = chars[read]
    #             write += 1
    #             num = read - left + 1
    #             if num > 1:
    #                 anchor = write
    #                 while num > 0:
    #                     chars[write] = str(num % 10)
    #                     write += 1
    #                     num //= 10
    #                 reverse(anchor, write - 1)
    #             left = read + 1
    #         print(chars)
    #     return write


if __name__ == '__main__':
    s = Solution()
    s.compress(["a", "a", "b", "b", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"])
