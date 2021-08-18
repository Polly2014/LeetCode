# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-14 17:26:26
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-14 18:20:54
from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        ans = set()
        match_list = [0] * n
        for x, y in pairs:
            match_list[x], match_list[y] = y, x
        for x, y in enumerate(match_list):
            if y_idx := preferences[x].index(y):
                u_list = preferences[x][:y_idx]
                for u in u_list:
                    v = match_list[u]
                    if preferences[u].index(x) < preferences[u].index(v):
                        ans.add(x)
        return len(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.unhappyFriends(4, [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], [[1, 3], [0, 2]]))
