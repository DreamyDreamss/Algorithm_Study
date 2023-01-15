from itertools import combinations

def solution(orders, course):
    answer = []
    counting_li = {}
    
    for i in range(0,26):
        counting_li[chr(ord('A')+i)] = 0
    
    for order in orders:
        for ch in range(len(order)):
            #print(order[ch])
            counting_li[order[ch]] += 1
            
    course_li= []
    for key in counting_li.keys():
        if counting_li[key] >= 2:
            course_li.append(key)
    
    print(course_li)
    for cnt in course:
        for i in combinations(course_li,cnt):
            answer.append(''.join(i))
    print(answer)
    answer.sort()
    return answer