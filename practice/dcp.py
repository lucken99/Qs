s = input()
# s = 'ABCDABCD.ABCDABCD.ABCDABCD.ABCDABCD'
rs = s.replace('.','')
rs = sorted(rs)

num = [ord(rs[0]), ord(rs[8]), ord(rs[17]), ord(rs[26])]
num1 =  bin(num[0]+63)[2:] + '.' + bin(num[1]+63)[2:] + '.' + bin(num[2]+63)[2:] + '.' + bin(num[3]+63)[2:]
print(num1)