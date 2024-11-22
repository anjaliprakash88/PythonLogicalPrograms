# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it
# Return the answer in an array
# INPUT: nums=[8, 1, 2, 2, 3]
# OUTPUT: [4, 0, 1, 1, 3]

nums = [7, 7, 7, 7]
y = []
for i in nums:
    count = 0
    for j in nums:
        if j < i:
            count += 1
    y.append(count)
print(y)
