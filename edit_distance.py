# Edit Distance
# Given two strings str1 and str2 and below operations that can performed on str1.
# Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.

# Insert
# Remove
# Replace
# All of the above operations are of equal cost.

# Examples:
# Input:   str1 = "geek", str2 = "gesek"
# Output:  1
# We can convert str1 into str2 by inserting a 's'.

# Input:   str1 = "cat", str2 = "cut"
# Output:  1
# We can convert str1 into str2 by replacing 'a' with 'u'.

# Input:   str1 = "sunday", str2 = "saturday"
# Output:  3
# Last three and first characters are same.  We basically
# need to convert "un" to "atur".  This can be done using
# below three operations. 
# Replace 'n' with 'r', insert t, insert a

# What are the subproblems in this case?
# The idea is process all characters one by one staring from either from left or right sides of both strings.
# Let us traverse from right corner, there are two possibilities for every pair of character being traversed.

# m: Length of str1 (first string)
# n: Length of str2 (second string)
# If last characters of two strings are same, nothing much to do. Ignore last characters and get count for remaining strings. So we recur for lengths m-1 and n-1.
# Else (If last characters are not same), we consider all operations on ‘str1’, consider all three operations on last character of first string, recursively compute minimum cost for all three operations and take minimum of three values.
# Insert: Recur for m and n-1
# Remove: Recur for m-1 and n
# Replace: Recur for m-1 and n-1

# Dynamic Programming implementation

def editDistance(str1, str2,  m, n):
    # Create a table to store results of subproblems
    dp = [[0 for i in range(n+1)] for i in range(m+1)]

    # fill dp[][] in bottom up manner
    for i in range(m+1):
        for j in range(n+1):

            # If first string is empty, only option is to 
            # insert all characters of second string
            if i==0:
                dp[i][j] == j # Min operations = j

            # If second string is empty, only option is to 
            # remove all characters of second string
            if j==0:
                dp[i][j] = i # min operations = i

            # if last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            # If last character are different, consider all 
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j-1],   #insert
                                    dp[i-1][j],  # remove
                                    dp[i-1][j-1]) # replace
    return dp[m][n]

str1 = "lastrewwwwwwwwwwwwwwm"
str2 = "lastremwwwwwwwwwwwww"

print(editDistance(str1, str2, len(str1), len(str2)))