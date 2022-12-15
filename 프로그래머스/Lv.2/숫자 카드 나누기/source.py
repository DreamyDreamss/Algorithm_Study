def solution(arrayA, arrayB):
    answer = 0
    minA,minB = min(arrayA),min(arrayB)
    sqmA,sqmB = int(minA**(0.5)),int(minB**(0.5))
    canA,canB = [minA],[minB]
    entireA,entireB = [],[]
    for i in range(2,sqmA+1):
        if i*i == minA:
            canA.append(i)
        elif minA%i == 0: 
            canA.append(i)
            canA.append(int(minA/i))
    
    for i in range(2,sqmB+1):
        if i*i == minA:
            canB.append(i)
        elif minB%i == 0: 
            canB.append(i)
            canB.append(int(minB/i))
    
    canA.sort(reverse=True)
    canB.sort(reverse=True)
    for ca in canA:
        flag=True
        for i in arrayA:
            if i%ca !=0:
                flag=False
                break
        if flag:
            entireA.append(ca)
    for cb in canB:
        flag=True
        for i in arrayB:
            if i%cb!=0:
                flag=False
                break
        if flag:
            entireB.append(cb)
    
    print(entireA,entireB)
    for cb in entireB:
        flag=True
        for idx in arrayA:
            if idx%cb ==0:
                flag=False
                break
        if flag and cb > answer: 
            answer = cb
            break
    
    for ca in entireA:
        flag=True
        for idx in arrayB:
            if idx%ca ==0:
                flag=False
                break
        if flag and ca > answer:
            answer = ca
            break
            
    return answer