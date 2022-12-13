def solution(id_list, report, k):
    answer = []
    pnt_dict = {}
    result_dict = {}
    
    for id in id_list:
        pnt_dict[id] = []
        result_dict[id] = 0
        
    for info in report:
        data = info.split(" ")
        if data[0] not in pnt_dict[data[1]]:
            pnt_dict[data[1]].append(data[0])
        
    for key,value in pnt_dict.items():
        if len(value) >= k:
            for li in value:
                result_dict[li] +=1
    
    for name in id_list:
        answer.append(result_dict[name])
        
    return answer