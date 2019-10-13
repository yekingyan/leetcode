#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
class Solution:
    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            # 如果当前数字大于0，则三数之和一定大于0，所以结束循环
            if nums[i] > 0:
                break
            # 排除数字重覆使结果重覆
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == 0:
                    tmp = [nums[i], nums[left], nums[right]]
                    res.append(tmp)
                    # 排除指针所指数字重覆使结果重覆
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    left += 1
        return res
