test = int(input())
for t in range(test):
    r1 = input().split()
    r2 = input().split()
    min_r1 = min(int(r1[0]),int(r1[1]))
    max_r1 = max(int(r1[0]),int(r1[1]))
    min_r2 = min(int(r2[0]),int(r2[1]))
    max_r2 = max(int(r2[0]),int(r2[1]))
    if max_r1 != max_r2:
        print("NO")
    else:
        if min_r1 + min_r2 == max_r1:
            print('YES')
        else:
            print('NO')