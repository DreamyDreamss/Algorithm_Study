def solution(k, tangerine):
    answer = 0
    tang_dict = {}
    
    for i in tangerine:
        if not i in tang_dict:
            tang_dict[i]=1
        else:
            tang_dict[i]+=1
    
    tt = sorted(tang_dict.values(),reverse=True)
    for i in range(0,len(tt)):
        k -= tt[i]
        if k<=0:
            return i+1