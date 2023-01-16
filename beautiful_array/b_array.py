n = int(input())
nums = [int(x) for x in input().split()]
nums.sort()
neg = nums[0]
pos = set()
zeros = set()
for i in range(n-1,1,-1):
    if nums[i] > 0:
        pos.add(str(nums[i]))
        break
    else:
        if nums[i]*nums[i-1] > 0:
            pos.add(str(nums[i]))
            pos.add(str(nums[i-1]))
            break
for num in nums:
    if str(num) not in pos and num != neg:
        zeros.add(str(num))
print(1,neg)
print(len(pos),' '.join(list(pos)))
print(len(zeros),' '.join(list(zeros)))