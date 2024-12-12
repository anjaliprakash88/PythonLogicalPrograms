# write a program to find the majority element in a given array of integer. A majority element is
# element that appears more than half of total elements in the array. if there's no majority elements
# the program should output "No majority element"
# example:
# input: 333344444231
# output: Majority element is 4

arr = "122835221"

# Step 1: Find a candidate for the majority element
candidate = None
count = 0

for element in arr:
    if count == 0:
        candidate = element
        count = 1
    elif element == candidate:
        count += 1
    else:
        count -= 1

# Step 2: Verify the candidate
if arr.count(candidate) >= len(arr) // 2 + 1:
    print(f"Majority element is {candidate}")
else:
    print("No majority element")
