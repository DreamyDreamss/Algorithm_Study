import math
MIN_RESULT = math.inf

def solution(x, y, n):
    
    def dfs(cx,cnt):
        global MIN_RESULT
        if cx>y:
            return
        elif cx==y:
            if cnt < MIN_RESULT:
                MIN_RESULT = cnt
            print(cx,cnt)
            return 
        
        dfs(cx+n,cnt+1)
        dfs(cx*2,cnt+1)
        dfs(cx*3,cnt+1)
        
        return 
    
    dfs(x,0)
    
    if MIN_RESULT == math.INF:
        return -1
    
    return MIN_RESULT