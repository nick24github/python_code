# min()
# max()
# finding minimum and maximum from a list
nums = [45,78,12,46,98,66,53,21,63,87,89,91]
# print(max(nums))
# print(min(nums))
max1 = nums[0]
for ele in nums:
    if ele>max1:
        max1 = ele
print("maximum value is :", max1)
for ele in nums:
    if ele<max1:
        max1 = ele
print("minimum value is :", max1)
