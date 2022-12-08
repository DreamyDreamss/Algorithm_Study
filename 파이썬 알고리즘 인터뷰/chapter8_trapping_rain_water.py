input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
output = 6

def trapping_rain(height):
		left , right = 0, len(height)-1
		max_left, max_right = 0, 0
		volumn = 0 
		
		while left < right:
				if max_left <= max_right : 
						max_left = max(height[left], max_left)
						volumn += max_left - height[left]
						left += 1
				else:
						max_right = max(height[right],max_right)
						volumn += max_right - height[right]
						right -= 1 
						
		return volumn
		
print(trapping_rain(input)) 