def cvt(n):
    cnt,tmp = 0,""
    for i in n:
        if i=="0":
            cnt+=1
    return (cnt,bin(len(n)-cnt)[2:])
    
def solution(s):
    zero_cnt,pros_cnt = 0,0
    while s!="1":
        c,s = cvt(s)
        pros_cnt += 1
        zero_cnt += c
    return [pros_cnt,zero_cnt]
    