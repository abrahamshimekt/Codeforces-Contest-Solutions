def top_row(matrix,top,left,right):
    top_row = []
    for c in range(left,right+1):
        top_row.append(matrix[top][c])
    return top_row
def left_col(matrix,top,bottom,left):
    left_col = []
    for row in range(bottom,top-1,-1):
        left_col.append(matrix[row][left])
        
    return left_col
    
def right_col(matrix,top,bottom,right):
    right_col = []
    for r in range(top,bottom+1):
        right_col.append(matrix[r][right])
        
    return right_col
    
def bottom_row(matrix,left,right,bottom):
    bottom_row = []
    for c in range(right,left-1,-1):
        bottom_row.append(matrix[bottom][c])
    return bottom_row
    
        
    
test = int(input())
for t in range(test):
    n = int(input())
    matrix = []
    for index in range(n):
        matrix.append(input())
   
    left = 0
    top = 0
    right = n-1
    bottom = n-1
    min_op = 0

    while left < right and top < bottom:
        
        t_row = top_row(matrix,top,left,right)
        r_col = right_col(matrix,top,bottom,right)
        b_row = bottom_row(matrix,left,right,bottom)
        l_col = left_col(matrix,top,bottom,left)
        
        
        for index in range(len(t_row)-1):
            ones = 0
            zeros = 0
            if int(t_row[index]) ==0:
                zeros +=1
            else :
                ones +=1
            if int(b_row[index]) ==0:
                zeros +=1
            else:
                ones +=1
            if int(r_col[index]) == 0:
                zeros +=1
            else:
                ones +=1
            if int(l_col[index]) == 0:
                zeros +=1
            else:
                ones +=1
                
            min_op += min(ones,zeros)
        
        left +=1
        right -=1
        top +=1
        bottom -=1

    print(min_op)