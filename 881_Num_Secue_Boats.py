# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-26 10:13:37
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-26 10:16:22
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        ans = 0
        people.sort()
        light, heavy = 0, n - 1
        while light <= heavy:
            if people[light] + people[heavy] > limit:
                heavy -= 1
            else:
                light, heavy = light + 1, heavy - 1
            ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.numRescueBoats([1, 2, 3], 3))
