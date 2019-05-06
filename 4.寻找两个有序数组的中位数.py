#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = sorted(nums1 + nums2)
        if len(merge) % 2 != 0:
            index = len(merge) // 2
            return merge[index]
        else:
            index = len(merge) // 2
            return (merge[index] + merge[index-1]) / 2
        

