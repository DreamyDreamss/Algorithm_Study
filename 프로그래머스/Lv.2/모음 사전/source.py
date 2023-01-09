ALPHA_LIST = []

def dfs(wd,cnt):
    global ALPHA_LIST
    alpha = ["A","E","I","O","U"]
    if cnt == 5:
        ALPHA_LIST.append(wd)
        return 0 
    
    ALPHA_LIST.append(wd)
    for i in alpha:
        dfs(wd+i,cnt+1)
  
def solution(word):
    global ALPHA_LIST
    dfs("",0)
    ALPHA_LIST.sort()

    return ALPHA_LIST.index(word)