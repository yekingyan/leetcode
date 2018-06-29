nums = [3,2,3]
target = 6
'''
i = 0
while i < len(nums):
    j = len(nums)-1
    while True:
        if nums[j] == target - nums[i] and j != i:
            print([i,j])
            break
        else:
            j = j - 1
        if j <= i:
            break
    i = i + 1
'''
for i in range(len(nums)):#历遍
    for j in range(len(nums)-1,i,-1):#另一数倒序历遍至i
        if nums[i] + nums[j] == target and i != j:
            print([i,j])