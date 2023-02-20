def solution(maps):
    answer = 0
    st,lb = (),()
    
    for i in len(maps):
        for j in len(maps[i]):
            if maps[i][j] == 'S':
                st = (i,j)
            if maps[i][j] == 'L':
                lb = (i,j)
                
    return answer