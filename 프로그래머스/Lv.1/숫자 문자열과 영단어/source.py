def solution(s):
    answer = ""
    
    num_dict = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    comp = ""
    for st in s:
        if st >= '0' and st <= '9':
            answer += st
        else:
            comp += st
            if len(comp) >=3 and comp in num_dict:
                answer += num_dict[comp]
                comp = ""
                
    return int(answer)