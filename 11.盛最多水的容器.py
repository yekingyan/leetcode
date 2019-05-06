#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while right > left:
            if height[left] > height[right]:
                h = height[right]
                area = h * (right-left)
                right -= 1
            else:
                h = height[left]
                area = h * (right-left)
                left += 1
            if area > max_area:
                max_area = area
        return max_area

            
