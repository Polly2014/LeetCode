# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-12-02 22:59:57
# @Last Modified by:   Polly
# @Last Modified time: 2021-12-02 23:07:58
from typing import List
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        desc = ('Gold Medal', 'Silver Medal', 'Bronze Medal')
        ans = ['']*len(score)
        score_sored = sorted(enumerate(score), key=lambda x: -x[1])
        for i,(idx,_) in enumerate(score_sored):
            ans[idx] = desc[i] if i<3 else str(i+1)
        return ans