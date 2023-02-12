import itertools
from collections import deque
import copy

max_result = 0

def calc(ol,st):
    global max_result
    for op in ol:
        while op in st:
            idx = st.index(op)
            st[idx-1] = str(eval(st[idx-1] + st[idx] + st[idx+1]))
            st.pop(idx+1)
            st.pop(idx)
    res = abs(int(st[0]))
    if max_result < res:
        max_result = res

def solution(expression):
    answer = []
    oper_set = ['*','+','-']
    for i in oper_set:
        if not i in expression:
            oper_set.remove(i)
    
    oper_set = list(itertools.permutations(oper_set,len(oper_set)))
    
    deque = []
    ditmp = ""
    for st in expression:
        if st.isdigit():
            ditmp += st
        else:
            deque.append((ditmp))
            deque.append(st)
            ditmp = ""
    deque.append((ditmp))

    for ol in oper_set:
        calc(ol,copy.deepcopy(deque))    
    
    print(max_result)
    return max_result

solution("100-200*300-500+20")