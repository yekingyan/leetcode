
def unique(nums: list) -> list:
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.pop(i)
        else:
            i = i + 1
    return nums


def unique2(nums: list) -> list:
    temp = []
    for i in nums:
        if i not in temp:
            temp.append(i)
    return temp


if __name__ == '__main__':
    a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    b = unique2(a)
    print(b)
