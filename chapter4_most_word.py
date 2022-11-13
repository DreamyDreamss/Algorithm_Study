import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def most_word(paragraph,banned):
		
		word = re.sub(r'[^\w\s]','',paragraph).lower()
		word_list = word.split()
		word_dict = dict()
		for word in word_list:
				if word in word_dict:
						word_dict[word]+=1
				else:
						word_dict[word] = 1
		
		for ban_key in banned:
				if ban_key in word_dict:
						del word_dict[ban_key]
		sorted_dict = sorted(word_dict.items(), key=lambda x:(-x[1], x[0]))
		
		return sorted_dict[0][0]
		
print(most_word(paragraph,banned))