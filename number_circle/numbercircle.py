n = int(input())
nums = [int(x) for x in input().split()]
nums.sort()
nums = [str(x) for x in nums]
if int(nums[0]) + int(nums[-2]) > int(nums[-1]):
    print("YES")
    print(" ".join(nums))
else:
    nums[-2],nums[-1] = nums[-1],nums[-2]
    if int(nums[-1]) + int(nums[-3]) > int(nums[-2]):
        print("YES")
        print(" ".join(nums))
    else:
        print("NO")