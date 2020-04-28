for i in range(2,9):
    for x in range(2,i):
        if i%x==0:
            print(i,'不是质数,因为它除了被本身整除外,还能被{:.0f}整除'.format(i/x))
            break
    else:
        print(i,"就是质数")

