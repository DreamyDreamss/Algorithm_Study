import copy

def compare(info,comp):
    tot = 0
    for i in range(0,11):
        if info[i] >= comp[i]:
            tot -= (10-i)
        else:
            tot += (10-i)
    
    print(tot)

    return tot

def dfs(idx,lim,info,comp):
        #print(f"idx: {idx},lim : {lim},comp : {comp}")
        if idx == 11 or lim<=0:
            print(comp)
            return 0
            #return compare(info,comp)
        tt = copy.deepcopy(comp)

        dfs(idx+1,lim,info,tt)

        if lim >= info[idx]+1:
            
            tt[idx] = info[idx]+1
            dfs(idx+1,lim-tt[idx],info,tt)
        

def solution(n, info):

    

    comp = [0,0,0,0,0,0,0,0,0,0,0]
    dfs(0,n,info,comp)

#info = [2,1,1,1,0,0,0,0,0,0,0]

solution(5,[2,1,1,1,0,0,0,0,0,0,0])