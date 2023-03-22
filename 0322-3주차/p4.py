import random

com = random.randrange(3)
user = int(input('가위0 바위1 보2 선택: '))
print('user= %d, com= %d' % (user, com))
if com == user:
    print('비겼습니다')
elif (user == 0 and com == 2) or (user > com):
    print('이겼습니다.')
else:
    print('졌습니다')