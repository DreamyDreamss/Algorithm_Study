from collections import deque 

def bfs(pos):
    deque = list()
    deque.append(pos)
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while deque:
        ps = deque.pop(0)
        for i in range(4):
            x= ps[0]+dx[i]
            y= ps[1]+dy[i]


            
def solution(maps):
    answer = 0
    st,lb = (),()
    visited = [[] for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            visited[i].append(0)
            if maps[i][j] == 'S':
                st = (i,j)
            if maps[i][j] == 'L':
                lb = (i,j)
    print(visited,st,lb)            
    while deque:

    
    return answer

maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
solution(maps)