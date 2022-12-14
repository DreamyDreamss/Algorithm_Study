def solution(absolutes, signs):
    answer = 0
    for idx in range(len(signs)):
        answer += absolutes[idx] if signs[idx] else -absolutes[idx]
    return answer