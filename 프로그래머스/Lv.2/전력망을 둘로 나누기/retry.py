import math

def dfs(pos,visited,graph,check_link):
    
    cnt = 1 
    visited[pos]= True

    for elem in graph[pos]:
        if not visited[elem] and check_link[pos][elem]:
            cnt += dfs(elem,visited,graph,check_link)

    return cnt

def solution(n, wires):
    answer = math.inf

    check_link  = [[True]*(n+1) for _ in range(n+1)]
 
    graph = [[] for _ in range(n+1)]
    
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for a,b in wires:
        
        visited = [False] * (n+1)

        check_link[a][b] = False
        a_cnt = dfs(a,visited,graph,check_link)
        b_cnt = dfs(b,visited,graph,check_link)
        check_link[a][b] = True

        cha = abs(a_cnt-b_cnt)
        if  answer > cha :
            answer = cha
    return answer

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))