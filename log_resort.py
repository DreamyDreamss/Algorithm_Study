logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

def log_spliter(logs) -> list:
		letters, digits = [], [] 
		for log in logs:
				content = "".join(log.split()[1:])
				if content.isdigit():
						digits.append(log)
				else:
						letters.append(log)
						
		letters.sort(key = lambda x: (x.split()[1:],x.split()[0]))
		return digits + letters

def log_spliter2(logs) -> list:
		letters, digits = [], [] 
		for log in logs:
				content = "".join(log.split()[1:])
				if content.isdigit():
						digits.append(log)
				else:
						letters.append(log)
						
		letters.sort(key = (x.split()[1:],x.split()[0]))
		return digits + letters
				
print(log_spliter2(logs))
