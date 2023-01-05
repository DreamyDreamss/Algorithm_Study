

# def solution(k, dungeons):
    
#     def dfs(k,visited,cnt):
#         global MAX_RESULT

#         for idx,value in enumerate(visited):
#             if value==False and k >= dungeons[idx][0]:
#                 visited[idx]=True
#                 dfs(k-dungeons[idx][1],visited,cnt+1)
#                 visited[idx]=False
        
#         #print(visited)

#         if cnt >= MAX_RESULT:
#             MAX_RESULT = cnt 
#         return 0


#     for idx,item in enumerate(dungeons):
#         visited = [False]*len(dungeons)
#         if item[0] <= k:
#             visited[idx] = True
#             dfs(k-item[1],visited,1)

#     return MAX_RESULT

MAX_RESULT = 0
visited = []

def solution(k, dungeons):
    
    def dfs(k,cnt):
        global MAX_RESULT
        if cnt > MAX_RESULT:
            MAX_RESULT = cnt

        for idx,value in enumerate(visited):

            if value==False and k >= dungeons[idx][0]:
                visited[idx]=True
                dfs(k-dungeons[idx][1],cnt+1)
                visited[idx]=False
        
        #print(visited)

        if cnt >= MAX_RESULT:
            MAX_RESULT = cnt 
        return 0

    global visited
    
    visited = [False]*len(dungeons)
    dfs(k,0)
    print(MAX_RESULT)
    return MAX_RESULT

solution(80,[[80,20],[50,40],[30,10]])