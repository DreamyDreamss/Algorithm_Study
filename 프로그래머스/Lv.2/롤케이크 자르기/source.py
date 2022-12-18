from collections import defaultdict

def solution(topping):
    answer = 0
    full_dict = defaultdict(int)
    right_set = set()

    for i in topping:
        full_dict[i] +=1

    for i in topping:
        full_dict[i] -= 1
        right_set.add(i)

        if full_dict[i] == 0:
            full_dict.pop(i)
        
        if len(full_dict) == len(right_set):
            answer +=1
            
    return answer