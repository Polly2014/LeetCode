# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-08-01 18:00:58
# @Last Modified by:   Polly
# @Last Modified time: 2021-08-01 18:39:40
from typing import List
from collections import Counter, OrderedDict


class Solution:
    # def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    #     count_list = [dict(Counter(i)).get(1, 0) for i in mat]
    #     count_dict = dict(zip(list(range(len(count_list))), count_list))
    #     count_dict_sorted = sorted(count_dict.items(), key=lambda x: x[1])
    #     return [count_dict_sorted[i][0] for i in range(k)]

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        count_list = [dict(Counter(i)).get(1, 0) for i in mat]
        count_list_sorted = sorted(enumerate(count_list), key=lambda x: x[1])
        return [count_list_sorted[i][0] for i in range(k)]
    '''
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        for i, m in enumerate(mat):
            m.append(i)
        mat.sort()
        return [mat[i][-1] for i in range(k)]
    '''


if __name__ == '__main__':
    s = Solution()
    print(s.kWeakestRows([[1, 1, 0, 0, 0],
                          [1, 1, 1, 1, 0],
                          [1, 0, 0, 0, 0],
                          [1, 1, 0, 0, 0],
                          [1, 1, 1, 1, 1]], 3))
    # l = [3, 1, 2, 3, 1]
    # print(sorted(enumerate(l), key=lambda x: x[1]))
