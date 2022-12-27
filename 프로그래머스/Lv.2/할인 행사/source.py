from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    for i in range(0,len(discount)-9):
        temp = Counter(discount[i:i+10])

        flag = True
        for idx,value in enumerate(want):
            if temp[value] < number[idx]:
                flag = False
        
        if flag:
            answer+=1
    print(answer)
    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

solution(want,number,discount)
