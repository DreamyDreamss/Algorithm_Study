def solution(numbers):
    answer = [0] * len(numbers)
    stack = []

    for idx in range(len(numbers)):
        
        while stack and numbers[stack[-1]] < numbers[idx]:
            answer[stack.pop()] = numbers[idx]

        stack.append(idx)
    while stack:
        answer[stack.pop()] = -1

    return answer

solution([-1, 5, 6, 6, -1, -1])