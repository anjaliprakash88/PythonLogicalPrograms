# You are given an array of nums containing distinct numbers in a random order. The numbers are supposed to be in the
# range from 1 to n, where n is the largest number in the array. Find all the missing numbers in this range and
# return them in increasing order.
# Example 1:
# Input: nums = [1, 3, 6, 8]

# Output: [2, 4, 5, 7]
# Explanation: The array should contain numbers from 1 to 8, but the numbers 2, 4, 5, and 7 are missing.
nums = [2, 5]
x =[]
for i in range(1, max(nums)):
    if i not in nums:
        x.append(i)

print(x)
