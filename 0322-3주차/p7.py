select = int(input('1. 입력한 수식 계산     2. 두 수 사이의 합계: '))

if select == 1:
    str = input('수식을 입력하세요: ')
    print('수식의 계산 값 = %d' % eval(str))