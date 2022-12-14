def yarksu_process(n):
    
    answer =0
    idx  = int(n**(0.5)) 

    for i in range(1,idx+1):
        if i*i == n:
            answer += 1
        elif n%i ==0:
            answer += 2
    
    if answer%2 == 0:
        return True
    else:
        return False

def solution(left, right):
    answer = 0

    for idx in range(left,right+1):
        val = idx if yarksu_process(idx) else -idx 
        answer += val
    return answer

