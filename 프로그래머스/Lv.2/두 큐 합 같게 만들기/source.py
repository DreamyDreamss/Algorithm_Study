from collections import deque

def solution(queue1, queue2):
    answer =0
    lens = len(queue1) + len(queue2)
    
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    
    if (sum1+sum2)%2 == 1:
        return -1
    h_sum = (sum1+sum2) / 2
        
    for _ in range(lens*2):
        if sum1 > h_sum:
            sum1 -= queue1[0]
            sum2 += queue1[0]
            queue2.append(queue1.popleft())
        elif sum2 > h_sum:
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2.popleft())
        else: 
            return answer
        
        answer += 1

    return -1

queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]

print(solution(queue1,queue2))