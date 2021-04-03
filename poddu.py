n = int(input())
if(n < 0):
	print("Wrong Input")
else:
	p=n*n*n*n
	flag = False
	while (n>0):
		if(n%10==p%10):
			n=n//10
			p=p//10
		else:
			print("FALSE")
			flag = True
			break
	if not flag:
		print("TRUE")

