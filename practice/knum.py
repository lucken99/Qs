def length(x, s, num):
    count = 0
    for i in range(len(s[num])):
        if s[num][i] < x:
            count += 1
        else:
            break
    return count
    

for _ in range(int(input())):
    l, r, k = map(int, input().split())
    
    ansr = 0
    ansl = 0
    s = [[0,1,2,3,4,5,6,7,8,9],[0,2,4,6,8],[0,3,6,9],[0,4,8],[0,5],[0,6],[0,7],[0,8],[0,9]]
    l = list(map(int, str(l)))
    r = list(map(int, str(r)))
    belowr = 0
    belowl = 0

    lr = len(r)
    ll = len(l)
    lk = len(s[k-1])

    if lr == 1:
        belowr = 1
    else:
        for i in range(1,lr):
            if i ==1:
                belowr += lk
                continue
            belowr += (lk-1)*(lk**(i-1))
    

    
    if ll == 1:
        belowl = 1
    else:
        for i in range(1,ll):
            if i == 1:
                belowl += lk
                continue
            belowl += (lk-1)*(lk**(i-1))

    if (r[0] > k) and
    

    last = 1
    for i in range(lr):
        if r[i] % k != 0:
            last = 0
            break
    print(ansr-ansl+last)
    

        







































    # k1 = {0,1,2,3,4,5,6,7,8,9}
    # k2 = {0,2,4,6,8}
    # k3 = {0,3,6,9}
    # k4 = {0,4,8}
    # k5 = {0, 5}
    # k6 = {0, 6}
    # k7 = {0, 7}
    # k8 = {0, 8}
    # k9 = {0, 9}
    

    


    
    # for i in range(len(r)):
    #     r[i] = length(r[i], s, k-1)
    # for i in range(len(r)):
    #     ansr += (r[i]*(len(s[k-1])**(len(r)-i-1)))


    # for i in range(len(l)):
    #     l[i] = length(l[i], s, k-1)
    # for i in range(len(l)):
    #     ansl += (l[i]*(len(s[k-1])**(len(l)-i-1)))

    
    # print(ansr-ansl+1)
    # ansr = len(s[k-1])
    # ansl = len(s[k-1])
    # if r[0] < k:
    # #calculate for all 1 to len(r)-1  digits
    #     for i in range(2, rn+1):
    #         ansr += (len(s[k-1])-1)*(len(s[k-1])**(i-1))
    #     for i in range(2, ln+1):
    #         ansl -= (len(s[k-1])-1)*(len(s[k-1])**(i-1))
    #     print(ansr - ansl)
        
        

    # else:
    #     f = []
    #     for i in s[k-1]:
    #         if (i > 0) and (i <= r[0]):
    #             f.append(i)

    #     for i in range(len(f)-1):
    #         ans += (len(s[k-1])**(rn-1))
    #     temp = 1
    #     for i in range(1,rn):
    #         temp *= (length(rn[i], s, k-1))
    #     ans += temp

    #     print(ans)







#     #dp = 

#     if k == 1:
#       for i in range(l, r+1):
#         count = 0
#         for j in str(i):
#           if int(j) not in k1:
#             break
#           else:
#             count += 1
#           if count == len(str(i)):
#             ans += 1
#     elif k == 2:
#       for i in range(l, r+1):
#         count = 0
#         for j in str(i):
#           if int(j) not in k2:
#             break
#           else:
#             count += 1
#           if count == len(str(i)):
#             ans += 1
#     elif k == 3:
#       for i in range(l, r+1):
#         count = 0
#         for j in str(i):
#           if int(j) not in k3:
#             break
#           else:
#             count += 1
#           if count == len(str(i)):
#             ans += 1
#     elif k == 4:
#       for i in range(l, r+1):
#         count = 0
#         for j in str(i):
#           if int(j) not in k4:
#             break
#           else:
#             count += 1
#           if count == len(str(i)):
#             ans += 1
#     elif k == 5:
#       for i in range(l, r+1):
#         count = 0
#         for j in str(i):
#           if int(j) not in k5:
#             break
#           else:
#             count += 1
#           if count == len(str(i)):
#             ans += 1
#     elif k == 6:
#       for i in range(l, r+1):
#         count = 0
#         for j in str(i):
#           if int(j) not in k6:
#             break
#           else:
#             count += 1
#           if count == len(str(i)):
#             ans += 1
#     elif k == 7:
#       for i in range(l, r+1):
#         count = 0
#         for j in str(i):
#           if int(j) not in k7:
#             break
#           else:
#             count += 1
#           if count == len(str(i)):
#             ans += 1
#     elif k == 8:
#       for i in range(l, r+1):
#         count = 0
#         for j in str(i):
#           if int(j) not in k8:
#             break
#           else:
#             count += 1
#           if count == len(str(i)):
#             ans += 1
#     elif k == 9:
#       for i in range(l, r+1):
#         count = 0
#         for j in str(i):
#           if int(j) not in k9:
#             break
#           else:
#             count += 1
#           if count == len(str(i)):
#             ans += 1
#     print(ans)








# def generator():
#     def convert(array):
#         i = 0
#         for e in array:
#             i *= 10
#             i += e
#         return i

#     def increment(array):
#         result = []
#         carry = True

#         for e in array[::-1]:
#             if carry:
#                 e += 1
#                 carry = False
#             if e > 6:
#                 e = 4
#                 carry = True
#             result = [e,] + result

#         if carry:
#             result = [4,] + result

#         return result

#     array = [4]
#     while True:
#         num = convert(array)
#         if num > 6665544441479: break

#         yield num
#         array = increment(array)
# count = 0
# for i in generator():
#   count += 1
# print(count)
    




        # ln = len(str(l))
        # rn = len(str(r))
        # sum1 = ln-1
        # sum2 = rn-1
        # ans = 0
        # if k>4:
        #    a = 0
        #    b  = 0
        #    for i in range(1, rn+1):
        #     a +=  (2**(i-1))
        #    for i in range(1,ln+1):
        #     b += (2**(i-1))

        # print(a-b)