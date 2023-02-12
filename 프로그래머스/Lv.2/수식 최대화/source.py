import itertools
from collections import deque
 
def solution(expression):
    answer = []
    oper_set = ['*','+','-']
    for i in oper_set:
        if not i in expression:
            oper_set.remove(i)
    
    oper_set = list(itertools.permutations(oper_set,len(oper_set)))
    #print(oper_set)

    deque = []
    operation = []
    ditmp = ""
    for st in expression:

        if st.isdigit():
            ditmp += st
        else:
            operation.append(int(ditmp))
            operand.append(st)
            ditmp = ""
    operation.append(int(ditmp))

    print(operand,operation)

    for ol in oper_set:
        for oper in ol:
            

    # ol = list()

    # def dfs(cnt):
    #     if cnt==3:
    #         calc(ol)
    #         return 
    #     for i in oper_set:
    #         if i in ol:
    #             continue
    #         ol.append(i)            
    #         dfs(cnt+1)           
    #         ol.pop()
      
    # def calc():

    #     stack = []
    #     print(expression)
    
    
    
    
    # dfs(0)


    return answer

solution("100-200*300-500+20")