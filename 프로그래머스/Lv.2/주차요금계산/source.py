from datetime import datetime
from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    
    dict = defaultdict(list)
    
    for data in records:
        dataset = data.split(' ')
        tt = datetime.strptime(dataset[0],'%H:%M')
        dict[dataset[1]].append(tt)
    srt_dict = sorted(dict.items())
    min_list = []
    for item in srt_dict:
        t_value = 0
        time_list = item[1]
        if len(time_list)%2 == 1:
            t = time_list.pop()
            t_value += (23*60 + 59) - (t.hour * 60 + t.minute)
        for elem in range(0,len(time_list),2):
            t_value += time_list[elem+1].hour * 60 + time_list[elem+1].minute - (time_list[elem].hour * 60 + time_list[elem].minute)
        min_list.append(t_value)
    
    for elem in min_list:
        pay_amt = fees[1] 
        elem -= fees[0]
        if elem>0:
            pay_amt += math.ceil(elem/fees[2]) * fees[3]
        answer.append(pay_amt)
    return answer