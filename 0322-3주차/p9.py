num = int(input('몇단까지 출력할까요? >> '))
for i in range(2,10):
    print('%d단:' % i, end=" ")
    for j in range(1,10):
        print('%dx%d=%d' % (i, j, i*j), end=" ")
        if num == j:
            break
    print()