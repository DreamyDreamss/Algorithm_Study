def solution(n, left, right):
    answer = []

    for i in range(left,right+1):
        print(i)
        answer.append(max(i%n,i//n)+1)
    return answer


solution(6,1,5)