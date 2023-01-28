def solution(s):
    answer = []
    s = s[2:-2]
    li  = s.split("},{")
    li.sort(key=len)
    for elem in li:
        nums = elem.split(",")
        for num in nums:
            if int(num) not in answer:
                answer.append(int(num))
    return answer

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")