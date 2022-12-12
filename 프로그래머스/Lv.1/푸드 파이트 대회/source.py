
def solution(food):
    answer = ''
    temp = ""
    
    for i in range(1,len(food)):
        for _ in range(food[i] // 2):
            temp = temp + str(i)
    answer =  temp+"0"+temp[::-1]
    
    return answer