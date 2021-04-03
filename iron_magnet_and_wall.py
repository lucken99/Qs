from queue import Queue
for _ in range(int(input())):
	n, k = map(int, input().split())
	s = input()

	p = k+1
	count = 0
	l, r  = 0, 0
	mag = Queue()
	iron = Queue()

	for i in range(n):
		if s[i] == 'M':
			mag.put(i)
		if s[i] == 'I':
			iron.put(i)
		if (s[i] == 'X') or (i == n-1):
			sheet = 0
		
			while (not mag.empty()) and ( not iron.empty()):
				sheet = 0
				l = min(mag.queue[0], iron.queue[0])
				r = max(mag.queue[0], iron.queue[0])
				for d in range(l, r+1):
					if s[d] == ':':
						sheet += 1

				if (p-abs(l-r)-sheet) > 0:
					count += 1
					mag.get()
					iron.get()
				elif mag.queue[0] < iron.queue[0]:
					mag.get()
				else:
					iron.get()
			while not mag.empty():
				mag.get()
			while not iron.empty():
				iron.get()
	print(count)

