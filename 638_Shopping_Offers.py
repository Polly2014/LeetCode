# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-10-24 20:31:18
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-24 22:21:00
from typing import List
from functools import lru_cache
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        m = len(special)
        def DFS(startIndex, needs):
            if startIndex==m:
                return sum(price[i]*needs[i] for i in range(n))
            cur_special = special[startIndex]
            ans = float('inf')
            nxt = []
            for i in range(n):
                if needs[i]>=cur_special[i]:
                    nxt.append(needs[i]-cur_special[i])
            if len(nxt)==n:
                # 选择大礼包,并且由于礼包无限买，因此 pos，而不是 pos + 1
                ans = min(ans, DFS(startIndex, nxt) + cur_special[n])
            # 不选择大礼包
            ans = min(ans, DFS(startIndex+1, needs))
            return ans
        return DFS(0, needs)

    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        # 过滤不需要计算的大礼包
        filter_special = []
        for sp in special:
            if sum(sp[i]*price[i] for i in range(n))>sp[-1]:
                filter_special.append(sp)

        @lru_cache(None)
        def DFS(cur_needs):
            min_price = sum(cur_needs[i]*price[i] for i in range(n))
            for cur_special in filter_special:
                special_price = cur_special[-1]
                nxt_needs = []
                for i in range(n):
                    if cur_special[i]>cur_needs[i]:
                        break
                    nxt_needs.append(cur_needs[i] - cur_special[i])
                if len(nxt_needs)==n:
                    min_price = min(min_price, DFS(tuple(nxt_needs))+special_price)
            return min_price
        return DFS(tuple(needs))

    # # 一句话
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
      return min([sum(p * n for p, n in zip(price, needs))] + [sp[-1] + self.shoppingOffers(price, special, [n - c for n, c in zip(needs, sp[:-1])]) for sp in special if not any(n < o for n, o in zip(needs, sp))])

if __name__=='__main__':
    from IPython import embed
    embed()