from copy import deepcopy

MAX_SERV = 0
MAX_AMT = []
def calc(users,nw_emo):
    #print("@@@@@@@@",nw_emo)
    global MAX_SERV
    global MAX_AMT
    serv = 0
    amt = 0
    tt = deepcopy(users)
    for idx in range(0,len(tt)):
        for emo in nw_emo:
            
            if tt[idx][0] <= emo[0]:
                tt[idx][1] -= emo[1]

    for idx in range(0,len(tt)):
        
        #print(tt[idx][0],   tt[idx][1],"@@")
        if tt[idx][1] > 0:
            amt += users[idx][1] - tt[idx][1]
        else:
            serv +=1

    if MAX_SERV < serv:
        MAX_SERV = serv
        MAX_AMT.clear()
        MAX_AMT.append(amt)
    elif MAX_SERV == serv:
        MAX_AMT.append(amt)

def solution(users, emoticons):
    answer = []
        
    users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
    emoticons = [1300, 1500, 1600, 4900]

    # users = [[40, 10000], [25, 10000]]
    # emoticons = [7000, 9000]

    def dfs(idx,nw_emo):
        if idx==len(emoticons):
            
            #print(nw_emo)
            calc(users,nw_emo)
            return

        for i in range(0,len(emoticons)):
            for j in range(10,41,10):
                nw_emo.append((j,(emoticons[idx] * (100-j))//100))
                dfs(idx+1,nw_emo)
                nw_emo.pop()

    dfs(0,[])
    
    return answer


solution(0,0)
print(MAX_SERV,max(MAX_AMT))

