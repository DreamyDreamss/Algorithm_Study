info_dict = [[[[[]for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(3)]

def convert(li):
    lang = {"cpp":0,"java":1,"python":2}
    pos = {"backend":0,"frontend":1}
    lev = {"junior":0,"senior":1}
    food = {"chicken":0,"pizza":1}
    
    return [lang[li[0]],pos[li[1]],lev[li[2]],food[li[3]],li[4]]

def counting_func(qry):
    lang = {"cpp":0,"java":1,"python":2}
    pos = {"backend":0,"frontend":1}
    lev = {"junior":0,"senior":1}
    food = {"chicken":0,"pizza":1}
    
    ans = []

    if qry[0]== "-":

    for a in range(3):


def solution(info, query):
    answer = []
    global info_dict

    for inf in info:
        li = inf.split(" ")
        idx = convert(li)
        info_dict[idx[0]][idx[1]][idx[2]][idx[3]].append(idx[4])

    for qry in query:
        li = qry.split(" ")
        while 'and' in li:
            li.remove('and') 
        counting_func(qry)

    print(info_dict)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"] 
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

solution(info,query)