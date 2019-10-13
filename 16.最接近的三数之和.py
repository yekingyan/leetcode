#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = {}
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                sum_num = nums[left] + nums[right] + nums[i]
                # 结果与目标值的距离
                if target < 0 < sum_num or sum_num < 0 < target:
                    distance = abs(target) + abs(sum_num)
                else:
                    distance = abs(target - sum_num)
                res[distance] = sum_num
                if sum_num < target:
                    left += 1
                else:
                    right -= 1
                # print(res)
        return res[min(res)]

# @lc code=end

