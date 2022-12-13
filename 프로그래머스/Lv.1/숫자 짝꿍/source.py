def solution(X, Y):
    answer = ''
    
    x_list = [0,0,0,0,0,0,0,0,0,0]
    y_list = [0,0,0,0,0,0,0,0,0,0]
    z_list = [0,0,0,0,0,0,0,0,0,0]
    for i in X:
        x_list[int(i)] +=1
    for i in Y:
        y_list[int(i)] +=1  
    for i in range(10):
        if x_list[i] !=0 and y_list[i]!=0:
            if x_list[i] > y_list[i]:
                z_list[i] = y_list[i]
            else:
                z_list[i] = x_list[i]
    result = []
    
    for i in range(9,-1,-1):
        for j in range(z_list[i]):
            answer += str(i)
    
    if answer == "":
        return "-1"
    elif answer[0] == "0":
        return "0"
    
    return answer