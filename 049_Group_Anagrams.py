# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-09-30 23:15:17
# @Last Modified by:   Polly
# @Last Modified time: 2021-09-30 23:30:50
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for ss in strs:
            mp[''.join(sorted(ss))].append(ss)
        return list(mp.values())


if __name__ == '__main__':
    s = Solution()
    s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
