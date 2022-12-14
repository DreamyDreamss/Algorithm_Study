def solution(new_id):
    answer = ''

    #step1 
    new_id = new_id.lower() 

    #step2
    for i in new_id:

        if not (i.isalnum() or i=='.' or i=='-' or i=='_'):
            new_id = new_id.replace(i,"")
    
    #step3
    tmp = []
    for i in new_id:
        if (len(tmp)>0 and tmp[-1]=='.' and i=='.'):
            pass
        else:
            tmp.append(i)
    new_id = "".join(tmp)
    
    #step4
    if len(new_id)>0 and new_id[0] =='.':
        new_id = new_id[1:len(new_id)]
    if len(new_id)>0 and new_id[-1] =='.':
        new_id = new_id[0:len(new_id)-1]
    
    #step5
    if len(new_id)==0:
        new_id = "a"
    
    #step6
    if len(new_id)>=16:
        new_id = new_id[0:16]
        if new_id[-1] =='.':
            new_id = new_id[0:len(new_id)-1]  

    #step7
    if len(new_id)<=2:
        st = new_id[-1]
        while len(new_id)<3:
            new_id += st
    
    return new_id
    print(new_id)
    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
#new_id = new_id[1:len(new_id)]
#print(new_id)
solution(new_id)
