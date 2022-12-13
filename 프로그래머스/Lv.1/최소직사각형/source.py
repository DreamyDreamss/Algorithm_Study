def solution(sizes):
    answer = 0
    short_list,long_list = [],[]
    for i in sizes:
        if i[0] > i[1]:            
            long_list.append(i[0])
            short_list.append(i[1])
        else:
            long_list.append(i[1])
            short_list.append(i[0])
            
    answer = max(short_list) * max(long_list)
    return answer