def solution(data, col, row_begin, row_end):
    answer = 0
    
    if col >1:
        data.sort(key= lambda x:(x[col-1],-x[0]))
    elif col==1:
        data.sort(key=lambda x:x[0])
        
    #print(data)
    res = []
    for row_idx in range(row_begin-1,row_end):
        tot = 0
        for c in data[row_idx]:
            tot += c % (row_idx+1)
        res.append(tot)
    #int(bin(tot)[2:])
    print(res)
    st = res[0]
    for r in res[1:]:
        st = st ^ r
    #print(int(str(st),2),int(st),res)
    return st

print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]],2,1,4))
