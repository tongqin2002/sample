# 制作九九乘法口诀表
for i in range(1,10):
    for j in range(1,10):
        print ("%d * %d = %2d" %(i,j,i*j),end = '  ')  # 一行之内用2个空格隔开
    print()  # 每行之间用换行隔开
