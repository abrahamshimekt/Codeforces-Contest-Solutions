n = int(input())
nums = [int(x) for x in input().split()]
nums_s = sorted(nums)
if nums == nums_s:
    print("yes")
    print(1,1)
else:
    start = 0
    end  = 0
    left = 0
    right = n -1
    s = []
    while left < right:
        if nums[left] == nums_s[left]:
            left +=1
        elif nums[right] == nums_s[right]:
            right -=1
        else:
            s = nums[left:right+1]
            start = left
            end = right
            break
    if start == end:
        print("yes")
        print(start+1,end+1)
    else:
        s = s[::-1]
        for i in range(len(s)):
            nums[i+start] = s[i]
        if nums == nums_s:
            print("yes")
            print(start+1,end+1)
        else:
            print('no')