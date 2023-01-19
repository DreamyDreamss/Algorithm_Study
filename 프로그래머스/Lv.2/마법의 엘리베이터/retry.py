def solution(storey):
    answer = 0
    
    while storey:
        end_num = storey % 10
        storey //= 10

        if end_num < 5:
            answer += end_num
        elif end_num > 5:
            answer += (10 - end_num)
            storey+= 1
        else: 
            answer += end_num
            if storey%10 >= 5:
                storey+=1
                
    return answer

solution(2558)
