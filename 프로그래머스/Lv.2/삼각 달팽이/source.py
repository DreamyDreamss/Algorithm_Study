def solution(n):
    answer = []
    pramide = [[[] for _ in range(idx+1)] for idx in range(n)]
    cur_num = 1
    row,col = -1,0
    
    for i in range(n,0,-3):
        for j in range(0,i):
    
            row+=1 
            pramide[row][col] = cur_num
            cur_num+=1     
        for j in range(0,i-1):
            col+=1 
            pramide[row][col] = cur_num
            cur_num+=1 
        for j in range(0,i-2):
            row-=1
            col-=1
            pramide[row][col] = cur_num
            cur_num+=1 

    for i in range(n):
        answer.extend(pramide[i]) 
    
    return answer

solution(8)
