def solution(n):
    answer = 0

    three_str = ""
    while n>=3:
        three_str += str(n%3)
        n//=3
    three_str += str(n)    

    for i in range(len(three_str)):
        answer += int(three_str[len(three_str)-1-i])*(3**i)

    return answer


print(solution(125))