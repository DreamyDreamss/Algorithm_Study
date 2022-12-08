nums = [2,7,11,5]  
target = 9 

def two_sum(nums,target):
		num_dict = {}
		for idx,value in enumerate(nums):
				num_dict[value] = idx
				
		for idx,value in enumerate(nums):
				if (target - value) in num_dict and idx != num_dict[target - value]:
						return [idx, num_dict[target - value]]
						
print(two_sum(nums,target))
				
		