n = int(input())
laps = []
for l in range(n):
    laps.append(input().split())
laps.sort()
f = False
for index in range(n-1):
    if laps[index][0] < laps[index+1][0] and laps[index][1] > laps[index+1][1]:
        f = True
        break
if f:
    print("Happy Alex")
else:
    print("Poor Alex")