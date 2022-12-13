def solution(a, b, n):
    answer = 0 
    emp_bot = n
    
    while emp_bot>=a:
        return_bot = (emp_bot//a) * b
        answer += return_bot
        emp_bot = emp_bot%a + return_bot
        
    return answer