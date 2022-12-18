def solution(k, ranges):
    
    answer = []
    y_list = []
    
    while k!=1:
        if k%2==0:
            h=k/2
            y_list.append((k+h)/2)
            k=h
        else:
            h = k*3 +1
            y_list.append((k+h)/2)
            k = h 
    for tup in ranges:
        st = tup[0]
        end = len(y_list) + tup[1]
        
        if st==0 and end==len(y_list):
            answer.append(sum(y_list))
        elif end < st:
            answer.append(-1.0)
        else:
            answer.append(sum(y_list[st:end]))
            
    return answer