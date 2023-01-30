def solution(board, moves):
    answer = 0
    stack = []

    for crain in moves:
        dole = 0
        for idx in range(len(board)):          
            if board[idx][crain-1] !=0:
                dole = board[idx][crain-1]
                board[idx][crain-1] = 0
                break
            
        if dole!=0:
            if len(stack)==0:
                stack.append(dole)
            else:
                if stack[-1] == dole:
                    stack.pop()
                    answer+=2
                else:
                    stack.append(dole)


    return answer