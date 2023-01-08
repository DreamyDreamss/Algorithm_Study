import re
from collections import deque

def bfs(user_pos,dataset,visited):
  dq = deque(user_pos)
  
  while len(dq) > 0:
    pos = dq.popleft()
    visited[pos[0]][pos[1]] = True
    #위 
    if pos[0] > 0 and visited[pos[0]-1][pos[1]] == False:
      if dataset[pos[0]-1][pos[1]] == "P":
        return 0
      elif dataset[pos[0]-1][pos[1]] == "O" and pos[2]==0:
        dq.append([pos[0]-1,pos[1],pos[2]+1])
    #아래
    if pos[0] < 4 and visited[pos[0]+1][pos[1]] == False:
      if dataset[pos[0]+1][pos[1]] == "P":
        return 0
      elif dataset[pos[0]+1][pos[1]] == "O" and pos[2]==0:
        dq.append([pos[0]+1,pos[1],pos[2]+1])
    #왼쪽
    if pos[1] > 0and visited[pos[0]][pos[1]-1] == False:
      if dataset[pos[0]][pos[1]-1] == "P":
        return 0
      elif dataset[pos[0]][pos[1]-1] == "O" and pos[2]==0:
        dq.append([pos[0],pos[1]-1,pos[2]+1])
    #오른쪽
    if pos[1] < 4and visited[pos[0]][pos[1]+1] == False:
      if dataset[pos[0]][pos[1]+1] == "P":
        return 0
      elif dataset[pos[0]][pos[1]+1] == "O" and pos[2]==0:
        dq.append([pos[0],pos[1]+1,pos[2]+1])
  return 1
    
      
def solution(places):
  answer = []

  for idx,dataset in enumerate(places):
    user_pos = []
    visited = [[False]*5 for _ in range(5)]
    #if idx!=1: 
    #  continue
    
    for row,value in enumerate(dataset):
      for col,value2 in enumerate(value):
        if value2 == "P":
          user_pos.append([row,col,0])
    answer.append(bfs(user_pos,dataset,visited))
  return answer

places=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

#solution(places)