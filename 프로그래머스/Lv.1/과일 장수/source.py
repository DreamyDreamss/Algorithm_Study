def solution(k, m, score):
    answer = 0
    score.sort()
    start = len(score) % m 
    
    for i in range(start,len(score),m):
        answer += score[i] * m
    
    return answer