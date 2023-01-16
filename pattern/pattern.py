num_patterns = int(input())
patterns = []
for pattern in range(num_patterns):
    patterns.append(input())
m = len(patterns)
n = len(patterns[0])
ans = ''
for col in range(n):
    disjoint = ''
    intersection = patterns[0][col]
    for row in range(1,m):
        if patterns[row][col] == '?':
            continue
        elif intersection == '?':
            intersection = patterns[row][col] 
        elif intersection != patterns[row][col] :
            disjoint = '?'
            intersection = ''
            break
    if intersection =='':
        ans +=disjoint
    elif intersection =='?':
        ans +='x'
    else:
        ans += intersection
    
print(ans)