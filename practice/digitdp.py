for _ in range(int(input())):
    l, r, k = map(int, input().split())
    
    ansr = 0
    ansl = 0
    global ans
    ans = 0
    #s = [[0,1,2,3,4,5,6,7,8,9],[0,2,4,6,8],[0,3,6,9],[0,4,8],[0,5],[0,6],[0,7],[0,8],[0,9]]
    k1 = {0,1,2,3,4,5,6,7,8,9}
    k2 = {0,2,4,6,8}
    k3 = {0,3,6,9}
    k4 = {0,4,8}
    k5 = {0, 5}
    k6 = {0, 6}
    k7 = {0, 7}
    k8 = {0, 8}
    k9 = {0, 9}
   

    if k == 1:
      for i in range(l, r+1):
        count = 0
        for j in str(i):
          if int(j) not in k1:
            break
          else:
            count += 1
          if count == len(str(i)):
            ans += 1
    elif k == 2:
      for i in range(l, r+1):
        count = 0
        for j in str(i):
          if int(j) not in k2:
            break
          else:
            count += 1
          if count == len(str(i)):
            ans += 1
    elif k == 3:
      for i in range(l, r+1):
        count = 0
        for j in str(i):
          if int(j) not in k3:
            break
          else:
            count += 1
          if count == len(str(i)):
            ans += 1
    elif k == 4:
      for i in range(l, r+1):
        count = 0
        for j in str(i):
          if int(j) not in k4:
            break
          else:
            count += 1
          if count == len(str(i)):
            ans += 1
    elif k == 5:
      for i in range(l, r+1):
        count = 0
        for j in str(i):
          if int(j) not in k5:
            break
          else:
            count += 1
          if count == len(str(i)):
            ans += 1
    elif k == 6:
      for i in range(l, r+1):
        count = 0
        for j in str(i):
          if int(j) not in k6:
            break
          else:
            count += 1
          if count == len(str(i)):
            ans += 1
    elif k == 7:
      for i in range(l, r+1):
        count = 0
        for j in str(i):
          if int(j) not in k7:
            break
          else:
            count += 1
          if count == len(str(i)):
            ans += 1
    elif k == 8:
      for i in range(l, r+1):
        count = 0
        for j in str(i):
          if int(j) not in k8:
            break
          else:
            count += 1
          if count == len(str(i)):
            ans += 1
    elif k == 9:
      for i in range(l, r+1):
        count = 0
        for j in str(i):
          if int(j) not in k9:
            break
          else:
            count += 1
          if count == len(str(i)):
            ans += 1
    print(ans)