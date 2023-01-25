T= int(input())
for t in range(T):
    nums = [int(x) for x in input().split()]
    nums.sort()
    print(nums[1])