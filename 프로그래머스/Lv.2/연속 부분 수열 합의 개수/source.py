def solution(elements):
    answer = 0
    ans_set = set()

    for i in range(1,len(elements)):
        for idx in range(0,len(elements)):
            t = elements[idx:idx+i]
            if idx+i > len(elements):
                ed = idx+i - len(elements)
                t = t+ elements[0:ed]
            ans_set.add(sum(t))
    ans_set.add(sum(elements))
    return len(ans_set)

elements = [0,1,2,3,4]
solution(elements)