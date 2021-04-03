# import string
# def hm(sentence):
# 	letters = set(string.ascii_letters+'!,.?-')
# 	count = 0
# 	flag = True
# 	i = 0
# 	while i < len(sentence):
# 		if sentence[i] == ' ':
# 			if flag:
# 				count += 1
# 			else:
# 				flag = True
# 			while sentence[i] == ' ':
# 				i += 1
# 		elif sentence[i] not in letters:
# 			flag = False
# 		i += 1
# 	return count+1



from string import ascii_letters
def hm(sentence):
	s = sentence.strip().split()
	ans = 0
	for i in s:
		flag = False
		for j in i:
			if (j not in ascii_letters) or (j not in [',', '-', '?', '!', '.']):
				flag = True
				break
		if not flag:
			ans += 1
	return ans
		

sentence = "he is a good programmer, he won 865 competitions, but sometimes he dont. What do you think? All test-cases should pass. Done-done?"
print(hm(sentence))