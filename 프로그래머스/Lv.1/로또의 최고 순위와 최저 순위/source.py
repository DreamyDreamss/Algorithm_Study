def solution(lottos, win_nums):
    answer = []
    mat = 0
    zero_cnt =0 
    for num in lottos:
        if num == 0:
            zero_cnt+=1
        elif num in win_nums:
           mat += 1
    max_cnt =6  if (mat + zero_cnt)==0 else 7 - (mat + zero_cnt)
    min_cnt =6  if mat==0 else 7 - mat

    return [max_cnt,min_cnt]


lottos = [44, 1, 0, 0, 31, 25]
win_nums=[31, 10, 45, 1, 6, 19]	

print(solution(lottos,win_nums))