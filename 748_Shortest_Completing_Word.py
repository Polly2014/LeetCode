# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-12-10 22:05:50
# @Last Modified by:   Polly
# @Last Modified time: 2021-12-10 22:07:25
from typing import List
from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        cnt = Counter(ch.lower() for ch in licensePlate)
        return min((word for word in words if not cnt - Counter(word)), key=len)
