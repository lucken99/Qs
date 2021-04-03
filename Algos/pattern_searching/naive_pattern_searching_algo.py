# In increasing order of running time 
# which i checked using time command in linux with t and w below.

def naive_p_search(s, p):
	m = len(p)
	n = len(s)
	for i in range(n-m+1):
		j = 0
		while j < m:
			if s[i+j] != p[j]:
				break
			j+=1
		if j== m:
			print(i)
			#break

# #naive_p_search('AABAACAADAABAAABAA', 'BAAC')
# # naive_p_search('ABABABCABABABCABABABC', 'ABABAC')
# # naive_p_search('AAAAAAAAAAAAAAAAAB', 'AAAAB')
t = "aabraacaadaabrca"
w = "aabrc"

naive_p_search(t, w) #O(nm)



# can we use python index function ?
# return index of first occurence of word from a given start 
# default start=0

# shortcut for above brute search or naive algo
# using python inbuild function.
# complexity O()

i = 0
while i < len(t)-len(w)+1:
	try:
		i = t.index(w, i)
	except:
		break
	print(i)
	i += 1



# def brute_search(w, t):
# 	if w == "":
# 		return -1
# 	wordlen = len(w)
# 	textlen = len(t)

# 	i = 0
# 	while i < textlen-wordlen+1:
# 		match = True
# 		for j in range(wordlen):
# 			if w[j] != t[i+j]:
# 				match = False
# 				break
# 		if match:
# 			print(str(i))
# 		i += 1

# 	return -1


# brute_search(w, t) #O(nm)