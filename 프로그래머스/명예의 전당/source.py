def solution(k, score):
    temp_list = []
    result = []
    for i in score:
        if len(temp_list) < k:
            temp_list.append(i)
        elif len(temp_list) == k and i>temp_list[0]:
            del(temp_list[0])
            temp_list.append(i)
        temp_list.sort()
        result.append(temp_list[0])
        
    return result