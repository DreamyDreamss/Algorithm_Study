def calc(a,b):
    A,B,E = a[0],a[1],a[2]
    C,D,F = b[0],b[1],b[2]

    if A*D-B*C ==0:
        print("##")
        return 0
    x = (B*F-E*D) / (A*D-B*C)
    y = (E*C-A*F) / (A*D-B*C)

    return (x,y)

def solution(line):
    answer = []
    int_set = set()
    for i in range(0,len(line)-1):
        for j in range(i+1,len(line)):
            res = calc(line[i],line[j])
            if res==0:
                continue
            else:
                #print(res)
                if res[0].is_integer() and res[1].is_integer():
                    int_set.add((int(res[0]),int(res[1])))
                    #print(res)
            # elif isinstance(res[0], int) and isinstance(res[1], int): 
            #     print(res)
            #     int_set.add((res[0],res[1]))

    up = max(int_set,key=lambda x:x[1])[1]
    down = min(int_set,key=lambda x:x[1])[1]
    left = min(int_set,key=lambda x:x[0])[0]
    right = max(int_set,key=lambda x:x[0])[0]
    print(up,down,left,right)

    for h in range(up,down-1,-1):
        st = ""
        for w in range(left,right+1):
            if (w,h) in int_set:
                st += "*"
            else:
                st += "."
        print(st)
        answer.append(st)

    return answer

solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])