import math
def find_hash(chess,m,n):
    
    for row in range(m):
        start = []
        for col in range(n):
            if chess[row][col] =="#":
                start.append((row+1,col+1))
        if len(start) == 2:
            return start
            
           
           
test = int(input())
 
for t in  range(test):
    input()
    chess = []
    for row in range(8):
        chess.append(input())
    start = find_hash(chess,8,8)
    
    left ,right = start
    if left[1] > right[1]:
        right,left = left ,right
    row = math.ceil((right[1]-left[1] + right[0]+left[0])/2)
    col = math.ceil((right[1]+left[1] + right[0] - left[0])/2)
    print(row,col)