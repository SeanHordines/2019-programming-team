num = int(input())

alpha = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
alpha2 = ['', '', 'twen', 'thir', 'for', 'fif', 'six', 'seven', 'eigh', 'nine']
suffixes = ['-', 'ty-', '-hundred-']
keywords = ['', 'thousand-', 'million-']


for i in range(num):
	amount = input()
	dollars = amount[:-3]
	cents = amount[-2:]
	string = ""
	m = len(dollars)//3
	n = len(dollars)%3
	temp = dollars[:n]
	if n > 0:
		keyword = keywords[m]
		loc = n
		for char in temp:
			val = int(char)
			suffix = suffixes[loc-1]	
			if val == 0:
				loc -= 1
			else:
				if loc == 2:
					if val == 1:
						val2 = int(temp[-1])
						if val2 == 0:
							string += 'ten-'
						elif val2 == 1:
							string += 'eleven-'
						elif val2 == 2:
							string += 'twelve-'
						else:
							string += alpha2[val2] + 'teen-'
						break
					else:
						string += alpha2[val] + suffix
				else:
					string += alpha[val] + suffix
				loc -= 1
		string += keyword
	for j in range(m):
		temp = dollars[n+(j*3):n+((j+1)*3)]
		keyword = keywords[m-j-1]
		loc = 3
		for char in temp:	
			val = int(char)
			suffix = suffixes[loc-1]
			if val == 0:
				loc -= 1
			else:
				if loc == 2:
					if val == 1:
						val2 = int(temp[-1])
						if val2 == 0:
							string += 'ten'
						elif val2 == 1:
							string += 'eleven'
						elif val2 == 2:
							string += 'twelve'
						else:
							string += alpha2[val2] + 'teen'
						break
					else:
						string += alpha2[val] + suffix
				else:
					string += alpha[val] + suffix
				loc -= 1
		if int(temp) > 0:
			string += keyword
	if len(string) > 0:
		if string[-1] == '-':
			string = string[:-1]
		string += " and " + str(int(cents)) + "/100 dollars"
	else:
		string = str(int(cents)) + "/100 dollar"
	print(string)
