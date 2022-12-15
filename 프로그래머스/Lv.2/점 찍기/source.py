def solution(k, d):
    answer = 0
    t1 = d*d   
    for i in range(0,d+1,k):
        answer += ((t1-(i**2))**(1/2))//k +1
    
    return answer