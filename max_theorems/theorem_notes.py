n , k = map(int,input().split())
theorems = list(map(int,input().split()))
mishka = list(map(int,input().split()))
initial = 0
for i in range(n):
    if mishka[i] == 1:
        initial += theorems[i]
 
l = 0
maxtheorem = initial
for r in range(n):
    if mishka[r] == 0:
        initial += theorems[r]
    while r-l+1 > k:
        if mishka[l] == 0:
            initial -= theorems[l]
        l += 1
    maxtheorem = max(maxtheorem,initial)
print(maxtheorem)