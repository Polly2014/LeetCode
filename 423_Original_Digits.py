# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-11-24 20:31:32
# @Last Modified by:   Polly
# @Last Modified time: 2021-11-24 21:06:08
from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        c = Counter(s)

        cnt = [0] * 10
        cnt[0] = c["z"]
        cnt[2] = c["w"]
        cnt[4] = c["u"]
        cnt[6] = c["x"]
        cnt[8] = c["g"]

        cnt[3] = c["h"] - cnt[8]
        cnt[5] = c["f"] - cnt[4]
        cnt[7] = c["s"] - cnt[6]
        
        cnt[1] = c["o"] - cnt[0] - cnt[2] - cnt[4]

        cnt[9] = c["i"] - cnt[5] - cnt[6] - cnt[8]

        return "".join(str(x) * cnt[x] for x in range(10))


if __name__=='__main__':
    s = Solution()
    print(s.originalDigits("owoztneoer"))