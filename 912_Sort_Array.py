# -*- coding: utf-8 -*-
# @Author: Polly
# @Date:   2021-07-18 17:36:03
# @Last Modified by:   Polly
# @Last Modified time: 2021-10-22 11:52:50

from typing import List
import random


class Solution:
    # 直观写法
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = random.randint(0, len(nums) - 1)
        flag = nums[mid]
        left = list(filter(lambda x: x <= flag, nums[0:mid] + nums[mid + 1:]))
        right = list(filter(lambda x: x > flag, nums[0:mid] + nums[mid + 1:]))
        return self.sortArray(left) + [flag] + self.sortArray(right)


    def randomized_partition(nums, left, right):
        pivot = random.randint(left,right)
        nums[pivot], nums[right] = nums[right], nums[pivot]
        pass

    # 递归调用快排，终止条件即下标相等或错位
    def randomized_quicksort(nums, left, right):
        if left>=right:
            return nums
        # mid=self.randomized_partition(nums, left, right)
        # self.randomized_quicksort(nums,left,mid-1)
        # self.randomized_quicksort(nums,mid+1, right)
        pivot = left
        i,j = left, right
        while i<j:
            while i<j and nums[j]>nums[pivot]:
                j-=1
            while i<j and nums[i]<nums[pivot]:
                i+=1
            nums[i],nums[j] = nums[j],nums[i]
        nums[pivot],nums[j] = nums[j],nums[pivot]
        randomized_quicksort(nums,left, j-1)
        randomized_quicksort(nums,j+1,right)

    # 标准写法
    def sortArray(self, nums: List[int])-> List[int]:
        self.randomized_quicksort(nums, 0,len(nums)-1)
        return nums


if __name__ == '__main__':
    # s = Solution()
    # print(s.sortArray([1, 2, 5, 9, 3, 6]))
    num = 7
    for i in range(10):
        print(num << i)
    # print(bin(7))
