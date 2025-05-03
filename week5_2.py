import sys
nums = [int(sys.stdin.readline()) for _ in range(9)]

total = sum(nums)
target = total - 100

found = False
a=0
b=0
for i in range(9):
    for j in range(i + 1, 9):
        if nums[i] + nums[j] == target:
            a, b = nums[i], nums[j]
            found = True
            break
    if found:

        break
nums.remove(a)
nums.remove(b)
result = []
# for num in nums:
#     if num == a or num == b:
#
#         if a == b:
#             a = b = -1
#         else:
#             if num == a:
#                 a = -1
#             else:
#                 b = -1
#         continue
#     result.append(num)

result.sort()
nums.sort()
for n in nums:
    print(n)