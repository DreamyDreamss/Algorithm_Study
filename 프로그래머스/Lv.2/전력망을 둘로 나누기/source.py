from collections import deque

visited = []

def pros(n,wires):
    global visited
    visited = [False] * n
    grp_list = []

    for idx,graph in enumerate(wires):
        st = wires[idx][0]
        if visited[st] == False:
            dfs(idx,wires)
            print(visited)

def dfs(idx,wires):
    global visited

    st = wires[idx][0]
    visited[st] = True
    arr = wires[idx][1]
    if visited[arr] ==False:
        for item in wires:
            if item[0] == arr:
                dfs(idx,wires)

def solution(n, wires):
    answer = -1
    wires = deque(wires)
    lens = len(wires)
    for i in range(lens):
        tmp = wires.popleft()
        pros(n,wires)
        wires.append(tmp)

    return answer

solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])