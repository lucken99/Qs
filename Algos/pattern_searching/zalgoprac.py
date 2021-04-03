# w = 'aab'
# t = 'baabaa'

#s = w+'$'+t
s = "aabcaabxaaaz"
s = "aabaacd"
s = "abababab"
s = "a"*10**3
a = [0]*len(s)
i = 1

# O(n^2) implementation of z array , see the naive implementation 
# in getZarr(). (efficient)
# while i < len(s):
#     count = 0
#     for j in range(len(s)):
#         if i+j >= len(s):
#             break

#         elif s[j] != s[i+j]:
#             break
#         else:
#             count += 1
		

#     a[i] = count
#     i += 1
	
		
# print(a)


# O(n) implementation of z array
def getZarr(string, z):
	n = len(string)

	# [L, R] make a window which matches
	# with prefix of s
	l, r, k = 0, 0, 0
	for i in range(1, n):
		# if i > R nothing matches so we will calculate
		# Z[i] using naive way

		if i > r:
			l, r = i, i

			while r < n and string[r-l] == string[r]:
				r += 1
			z[i] = r-l
			r -= 1
		else:
			# k = i-L so k correspond to number which
			# matches in [L, R] interval.
			k = i- l

			# if Z[k] is less than remaining interval 
            # then Z[i] will be equal to Z[k]. 
            # For example, str = "ababab", i = 3, R = 5 
            # and L = 2 
			if z[k] < r - i + 1:
				z[i] = z[k]
			else:
				# else start from R and check manually
				l = i
				while r < n and string[r-l] == string[r]:
					r += 1
				z[i] = r-l
				r -= 1
s = "dabra$dabrcadabradabra"
z = [0 for i in range(len(s)) ]
getZarr(s, z)
print(z)
			