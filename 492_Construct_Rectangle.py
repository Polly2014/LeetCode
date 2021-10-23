# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-23 19:33:17
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-23 19:35:48
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = int(sqrt(area))
        while area % w:
            w -= 1
        return [area // w, w]
