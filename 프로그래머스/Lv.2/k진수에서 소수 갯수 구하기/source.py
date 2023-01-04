def solution(n, k):
    answer = 0
    convert_num = ""
    while n>k:
        convert_num += str(n%k)
        n= n//k
    convert_num += str(n)
    
    print(convert_num[::-1])
    sp_list = convert_num[::-1].split('0')
    num_list = [int(x) for x in sp_list if x != ''] 
    
    for num in num_list:
        flag = True
        if num == 1:
            continue
        for i in range(2,round(num**0.5)+1):
            if num%i == 0:
                flag = False
                break
        if flag:
            #print(num)
            answer+=1
    print(num_list)
    return answer
