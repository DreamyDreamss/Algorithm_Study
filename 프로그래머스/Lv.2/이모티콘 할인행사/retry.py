from copy import deepcopy

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
dis_emo = [[((idx+1)*10,int(emoticons[k]* (100-(idx+1)*10)/100)) 
            for idx in range(len(emoticons))] for k  in range(len(emoticons))]

#print(dis_emo)
MAX_CNT,MAX_AMT = 0,0

def dfs(emo_idx,user):
    global dis_emo

    if len(dis_emo) == emo_idx:
        global MAX_CNT,MAX_AMT,users
        #print(user)
        amt,cnt = 0,0
        for i in range(len(user)):
            if user[i][1] >0:   
                amt += users[i][1] - user[i][1]
            else:
                cnt += 1
        if MAX_CNT < cnt:
            MAX_CNT = cnt
            MAX_AMT = 0
        if MAX_CNT == cnt and MAX_AMT < amt:
            MAX_AMT = amt

        return 

    for dis_idx in dis_emo[emo_idx]:
        t = deepcopy(user)

        for item in t:
            if item[0] <= dis_idx[0]:      
                item[1] -= dis_idx[1]
        dfs(emo_idx+1,t)
        
dfs(0,users)
print(MAX_CNT,MAX_AMT)
