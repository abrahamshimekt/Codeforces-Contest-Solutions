contest_num = int(input())
contests = input().split()

performance = 0

min_score = int(contests[0])
max_score = int(contests[0])

for index in range(1,contest_num):
    if int(contests[index]) > max_score:
        performance +=1
        max_score = int(contests[index])
    elif int(contests[index]) < min_score:
        performance += 1
        min_score = int(contests[index])
print(performance)
    
