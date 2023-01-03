import copy
MAX_LIST = []
MAX_SCORE = -100

def compare(info,comp):
    enemy_score = 0
    my_score = 0  
    for i in range(11):
        if (info[i]==0 and comp[i]==0): 
            pass
        else:
            if info[i] >= comp[i]:
                enemy_score += (10-i)
            elif info[i] < comp[i]:
                my_score += (10-i)
    #print(comp,"###", my_score - enemy_score,my_score,enemy_score)    

    return my_score - enemy_score

def dfs(idx,lim,info,comp):
    global MAX_LIST, MAX_SCORE

    if idx == 11:
        if lim!=0:
            comp[10] = lim
        comp_score = compare(info,comp)

        if MAX_SCORE < comp_score:
            MAX_LIST.clear()
            MAX_SCORE = comp_score
            MAX_LIST.append(comp)

        elif MAX_SCORE == comp_score:
            MAX_LIST.append(comp)
        return 0

    tt = copy.deepcopy(comp)
    dfs(idx+1,lim,info,tt)
    if lim >= info[idx]+1:
        tt[idx] = info[idx]+1
        dfs(idx+1,lim-tt[idx],info,tt)
        
def solution(n, info):
    comp = [0,0,0,0,0,0,0,0,0,0,0]
    dfs(0,n,info,comp)
    
    if MAX_SCORE <= 0:
        return [-1]
    
    MAX_LIST.sort(key= lambda x:x[::-1],reverse=True)
    
    return MAX_LIST[0]

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))