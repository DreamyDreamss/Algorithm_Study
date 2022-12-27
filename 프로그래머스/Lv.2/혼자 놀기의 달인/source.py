from collections import defaultdict

def dfs(box_dict,tmp_list,cards,idx):
    if box_dict[idx]==0:
        box_dict[idx] +=1
        tmp_list.append(idx)
        dfs(box_dict,tmp_list,cards,cards[idx])
    
    return tmp_list
def solution(cards):
    cards.insert(0,0)
    box_dict = defaultdict(int)
    group_list = []

    for i in range(1,len(cards)):
        if box_dict[i]==0:
            box_dict[i] +=1
            tmp_list = [i]
            tmp_list = dfs(box_dict,tmp_list,cards,cards[i])
            print(tmp_list,"##")
            group_list.append(tmp_list)

    group_list.sort(key=len,reverse=True)
    
    return len(group_list[0])*len(group_list[1])
    
cards = [8,6,3,7,2,5,1,4]
cards = [2,1]

print(solution(cards))
