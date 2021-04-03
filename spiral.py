def spiral_matrix(a, m, n):
	top = 0
	bottom = m-1
	left = 0
	right = n-1

	direction = 0

	while top <= bottom and left <= right:
		if direction == 0:
			for i in range(left, right+1):
				print(a[top][i])
			top += 1
			direction = 1
		elif direction == 1:
			for i in range(top, bottom+1):
				print(a[i][right])
			right -= 1
			direction = 2
		elif direction == 2:
			for i in range(right, left-1, -1):
				print(a[bottom][i])
			bottom -= 1
			direction = 3
		elif direction == 3:
			for i in range(bottom, top-1, -1):
				print(a[i][left])
			left += 1
			direction = 0

spiral_matrix([[1,2,5],[5,7,8],[6,9,8]], 3,3)
