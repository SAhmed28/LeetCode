
nums =[3,2,4]
target = 6
# print(len(nums))

for i in range (len(nums)):
    for j in range (i,len(nums)):
        initial = nums[i]
        if j > 0 and i!=j:
            sum = initial + nums[j]
            if sum == target:
                print(i,j)
