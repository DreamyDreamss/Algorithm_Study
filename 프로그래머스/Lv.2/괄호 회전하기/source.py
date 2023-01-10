from collections import deque

def calc(s): 
    stack = []  
    for st in s:
        #print(st,stack)
        if st == "[" or st=="(" or st=="{":
            stack.append(st)        
        elif len(stack) >0:
            last = stack.pop()
            if last == "[" and (st == ")" or st == "}"):
                return 0
            elif last == "(" and (st == "]" or st == "}"):
                return 0
            elif last == "{" and (st == ")" or st == "]"):
                return 0
        else:
            return 0
    return 1

def solution(s):
    answer = 0

    for i in range(len(s)):
        #print(i)
        ss = deque(s)
        ss.rotate(i)
        if calc(ss):
            answer +=1
    print(answer)
    return answer

solution("(")