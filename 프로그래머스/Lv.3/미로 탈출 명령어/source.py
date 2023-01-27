import sys

sys.setrecursionlimit(100000)
def solution(n, m, x, y, r, c, k):
    answer = []
    dx = [0,-1,1,0]
    dy = [1,0,0,-1]
    ap = ['d','l','r','u']
    flag = [0]    

    def dfs(pos,root,cnt):
        if flag[0] or abs(pos[0] - c) + abs(pos[1] - r) + cnt > k:
            return 
        if cnt==k:
            if pos[0]==c and pos[1] ==r:
                answer.append(root)
                flag[0]=1
            return

        for i in range(4):
            nx,ny = pos[0]+dx[i],pos[1]+dy[i]
            if 0<nx<=m and 0<ny<=n:
                dfs((nx,ny),root+ap[i],cnt+1)
            
    z = k - (abs(x - r) + abs(y - c))
    if z < 0 or z % 2 != 0:
        return 'impossible'
    
    dfs((y,x),"",0)
    
    if not answer:
        return "impossible"
    else:
        return answer[0]

