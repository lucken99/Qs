#kmp O(n+m)

def create_aux(w):
	lenw = len(w)
	aux = [0]*lenw

	# for index 0, aux[0] wil always be 0
	# so starting from index 1
	i = 1

	# m can also be viewed as index of first mismatch

	m = 0

	while i < lenw:
		# prefix = suffix till m-1
		if w[i] == w[m]:
			m += 1
			aux[i] = m
			i += 1

		# when there is a mismatch
		# we will check the index of previous
		# possible prefix

		elif w[i] != w[m] and m != 0:
			# note that we do not increment i here
			m = aux[m-1]
		else:
			# m = 0, we move to the next letter
			# there was no any prefix found which
			# is equal to the suffix for index i

			aux[i] = 0
			i += 1
	return aux

# w = "aca"
# t = "acfacabacabacacdk"
t = "l"*10**7
w = "lll"

lenw = len(w)
lent = len(t)

aux = create_aux(w)

# counter for word
i = 0
# counter for text
j = 0

while j<lent:
	# we need to handle 2 condition when there is a mismatch
	if w[i] != t[j]:
		if i == 0:
			# starting again from the next char in t.
			j += 1
		else:
			# aux[i-1] will tell from where to compare next
			# and no need to match for w[0..aux[i-1] - 1].
			# they will match anyway, that's  what kmp is about.
			i = aux[i-1]
	else:
		i += 1
		j += 1
		if i == lenw:
			print(str(j-i))

			# if we want to find more patterns, we can 
			# continue as if no match was found at this point.
			i = aux[i-1]


