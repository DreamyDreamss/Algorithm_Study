ALPHA_LIST = []

def dfs(wd,cnt):
    global ALPHA_LIST
    alpha = ["A","E","I","O","U"]
    if cnt == 5:
        ALPHA_LIST.append(wd)
        return 0 
        print(wd)
    
    ALPHA_LIST.append(wd)
    for i in range(alpha):
        dfs(wd+i,cnt+1)
    
    
def solution(word):
    
    dfs("",0)
    
    answer = 0
    return answer