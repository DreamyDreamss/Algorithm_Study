input = ["eat","tea","tan","ate","nat","bat"]


def group_anagrams(input):
		anagrams = dict()				
		for word in input:				
				sorted_word = "".join(sorted(word))
				if sorted_word in anagrams: 
						anagrams[sorted_word].append(word)
				else:
						anagrams[sorted_word] = [word]
		
		return list(anagrams.values())
		
print(group_anagrams(input))