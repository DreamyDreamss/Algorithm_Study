from itertools import combinations

def solution(orders, course):
    answer = []
    counting_li = {}
    
    for order in orders:
        li = list(order)
        li.sort()
        for lens in course:
            for st in combinations(li,lens):
                wd = ''.join(st)
                if wd in counting_li:
                    counting_li[wd] += 1
                else:
                    counting_li[wd] = 1
    #print(counting_li)            
    course_li= []
    
    for lens in course:
        tmp = []
        max_value = 0
        for key,value in list(counting_li.items()):
            if value < 2:
                del counting_li[key]    
            elif len(key) == lens:
                if max_value < value:
                    max_value = value
                    tmp.clear()
                    tmp.append(key)
                elif max_value == value:
                    tmp.append(key)
                
        answer.extend(tmp)
    answer.sort()
    return answer

#solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])