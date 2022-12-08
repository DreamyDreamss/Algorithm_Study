input = [1,4,3,2]

def array_partition(nums):
		sum = 0
		pair = []
		nums.sort()
		
		for i, n in enumerate(nums):
				if i % 2 == 0:
						sum += n
		
		return sum
		
		
print(array_partition(input))
		