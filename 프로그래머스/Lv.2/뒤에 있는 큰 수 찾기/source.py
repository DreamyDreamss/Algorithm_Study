def solution(numbers):
    answer = []
    dic = dict()
    
    #for idx,num in enumerate(numbers):
    #    dic[idx] = num
    
    #print(dic)
    
    len_num = len(numbers)
    nxt_max_num = (0,-1)
    
    for idx,num in enumerate(numbers):
        flag = 1
        st = idx + 1
        if num > nxt_max_num[1]:
            st = nxt_max_num[0]+1
            
        for comp_idx in range(st,len_num):
            #print(comp)
            comp_num = numbers[comp_idx]
            if num < comp_num:
                answer.append(comp_num)
                nxt_max_num = (comp_idx,comp_num)
                flag = 0
                break
        if flag:
            answer.append(-1)
    
    #print(answer)
    return answer