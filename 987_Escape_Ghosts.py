# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-22 12:29:48
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-22 12:36:06
from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        base_length = abs(target[0]) + abs(target[1])
        ghost_length = [abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) for ghost in ghosts]
        return all([gl > base_length for gl in ghost_length])


if __name__ == '__main__':
    s = Solution()
    print(s.escapeGhosts([[1, 0], [0, 3]], [0, 1]))
