input = "abcdedcbffwaa"

def longest_palindrome(input):
		# 팰린드롬 판별 내장함수(투포인터)
		def pros(lpoint,rpoint):
				while lpoint >=0 and rpoint < len(input) and input[lpoint] == input[rpoint]:
						lpoint -= 1 
						rpoint += 1
				return input[lpoint+1:rpoint] 
		
		if len(input)==1 or (input == input[::-1]):
				return input
		
		result = ''
		# 짝수케이스/홀수케이스
		for idx in range(len(input)-1):
				result = max(pros(idx,idx+1), pros(idx,idx+2), result, key = len)
				
		return result	

print(longest_palindrome(input))