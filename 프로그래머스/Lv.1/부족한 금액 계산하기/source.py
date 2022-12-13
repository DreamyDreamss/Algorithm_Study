def solution(price, money, count):
    answer = (count * (price+(price * count)))/2 - money 
    answer = answer if answer>=0 else 0
    return answer