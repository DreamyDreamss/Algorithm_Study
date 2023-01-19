
def solution(storey):
    answer = 0
    #storey = 9942
    st = list(str(storey))[::-1]
    print(st)
    idx = 0 

    while st:
        if idx>=len(st):
            break
            
        val = int(st[idx])
        if val<=5:
            answer += val
            idx+=1
        elif val>6:
            answer += 10-val
            t = st[idx+1:]
            st = list(str(int("".join(t[::-1]))+1))[::-1]
            idx = 0
         
        print(st,answer)
        
    return answer

#solution(16)

a=[1,2,3]

print(a[4:])