for i in range(2,10):
    print('%d단:' % i, end=" ")
    for j in range(1,10):
        if  j == 5:
            continue #5e단이 업승ㅁ
        print('%dx%d=%d' % (i, j, i*j), end=" ")
    print()