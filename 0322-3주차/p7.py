select = int(input('1. 입력한 수식 계산     2. 두 수 사이의 합계: '))

if select == 1:
    str = input('수식을 입력하세요: ')
    print('수식의 계산 값 = %d' % eval(str))
elif select == 2:
    sum = 0
    n1 = int(input('두 수를 입력하세요(1/2): '))
    n2 = int(input('두 수를 입력하세요(2/2): '))
    for i in range (n1, n2+1):
        sum += i 
    print('두 수 사이의 합계 = %d' % sum)