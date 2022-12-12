def solution(ingredient):
    answer = 0
    burger = [1,2,3,1]

    stack = []
    for idx,i in enumerate(ingredient):
        stack.append(i)
        if len(stack)>=4:
            if stack[len(stack)-4:len(stack)+1] == burger:
                for _ in range(4):
                    stack.pop()
                answer+=1

    return answer