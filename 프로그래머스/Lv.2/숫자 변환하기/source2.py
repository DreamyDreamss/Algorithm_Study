from collections import deque
import math

def solution(x, y, n):
    answer = math.inf
    que = deque([(x,0)])
    set =  {x}
    while que:
        val = que.popleft()
        
        if val[0] == y and val[1] < answer:
            answer = val[1]
            #print(val)
        if val[0]*2 <= y and val[0]*2 not in set:
            que.append((val[0]*2,val[1]+1))
            set.add(val[0]*2)
        if val[0]*3 <= y and val[0]*3 not in set:
            que.append((val[0]*3,val[1]+1))
            set.add(val[0]*3)    
        if val[0]+n <= y and val[0]+n not in set:
            que.append((val[0]+n,val[1]+1))
            set.add(val[0]+n)    
    if answer == math.inf:
        return -1
    
    return answer