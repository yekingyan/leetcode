#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode-cn.com/problems/search-insert-position/description/
#
# algorithms
# Easy (42.57%)
# Total Accepted:    29.5K
# Total Submissions: 69.2K
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 
# 你可以假设数组中无重复元素。
# 
# 示例 1:
# 
# 输入: [1,3,5,6], 5
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: [1,3,5,6], 2
# 输出: 1
# 
# 
# 示例 3:
# 
# 输入: [1,3,5,6], 7
# 输出: 4
# 
# 
# 示例 4:
# 
# 输入: [1,3,5,6], 0
# 输出: 0
# 
# 
#


class Solution:
    def searchInsert(self, nums: 'List[int]', target: int) -> int:
        last = 1
        for index_, i in enumerate(nums):
            if target < i or target == i:
                return index_
            last = index_
        return last+1


if __name__ == '__main__':

    s = Solution()
    func = s.searchInsert

    param2 = [
        [([1, 3, 5, 6], 5), 2],
        [([1, 3, 5, 6], 2), 1],
        [([1, 3, 5, 6], 0), 0],
        [([1, 3, 5, 6], 7), 4],
    ]

    def test(condition, e):
        if not condition:
            print(e)

    def two_param_to_test(_function, _params):
        for index, i in enumerate(_params):
            param1 = i[0][0]
            param2 = i[0][1]
            exp = i[1]
            test(_function(param1, param2) == exp, f'err: {index}-{i}')

    two_param_to_test(func, param2)
