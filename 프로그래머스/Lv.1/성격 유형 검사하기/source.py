def solution(survey, choices):
    answer = ''
    sco_dict = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    
    ans_cnt = len(survey)
    for idx in range(ans_cnt):
        if choices[idx] < 4:
            sco_dict[survey[idx][0]] += 4-choices[idx]
        elif choices[idx] > 4:
            sco_dict[survey[idx][1]] += choices[idx]-4

    if sco_dict["R"] >= sco_dict["T"] :
        answer += "R"
    else:
        answer += "T"
    if sco_dict["C"] >= sco_dict["F"]:
        answer += "C"
    else:
        answer += "F"
    if sco_dict["J"] >= sco_dict["M"]:
        answer += "J"
    else:
        answer += "M"
    if sco_dict["A"] >= sco_dict["N"]:
        answer += "A"
    else:
        answer += "N"
        
    return answer