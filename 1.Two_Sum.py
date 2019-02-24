
def two_sum1(target, nums):
    for i in range(len(nums)):
        # 另一数倒序历遍至i
        for j in range(len(nums)-1, i, -1):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]


def two_sum2(target, nums):
    d = {}
    for i, num in enumerate(nums):
        n = target - num
        if n in d:
            return [d[target - num], i]
        d[num] = i
    return None


def two_sum3(target, nums):
    d = []
    for i, num in enumerate(nums):
        n = target - num
        if n in nums and i != nums.index(n):
            d.append([i, nums.index(n)])
            return d[0]


def text():
    nums = [3, 2, 3]
    target = 6
    l1 = two_sum1(target, nums)
    l2 = two_sum2(target, nums)
    l3 = two_sum3(target, nums)
    print(l1, l2, l3)


if __name__ == '__main__':
    text()