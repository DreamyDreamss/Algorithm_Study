from collections import deque

def bfs(mat):
    user_pos = []
    
    for i in range(5):
        for j in range(5):
            if mat[i][j] == "P":
                user_pos.append((i,j))

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    for s in user_pos:
        queue = deque([s])
        visited = [[0]*5 for _ in range(5)]
        distance = [[0]*5 for _ in range(5)]

        while queue:
            y,x = queue.popleft()
            visited[y][x] = 1

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                
                if 0<=ny<5 and 0<=nx<5 and visited[ny][nx]==0:
                    if mat[ny][nx] == "O" and distance[y][x] ==0:
                        queue.append((ny,nx))
                        distance[ny][nx] = distance[y][x]+1
                    elif mat[ny][nx] == "P":
                        return 0    
    return 1

def solution(places):
    answer = []

    for i in places:
        answer.append(bfs(i))
    print(answer)
    return answer

