def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        n_count=0
        if i == 1:
            n_count = 1
        elif i == 2 or i == 3:
            n_count = 2
        else:
            for j in range(1,int(i**(1/2)+1)):
                if i%j==0:
                    if j*j == i:
                        n_count += 1 
                    else:
                     n_count += 2
        if n_count > limit:
            answer += power
        else: 
            answer += n_count
        
    return answer