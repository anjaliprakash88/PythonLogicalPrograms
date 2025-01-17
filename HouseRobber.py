
# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses
# have security systems connected and it will automatically contact the police
# if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

nums = [2, 7, 9, 3, 1]
sum = 0
if len(nums) == 2:
    print(max(nums))
else:
    for i in nums[::2]:
        sum = sum + i
    print(sum)