# 从0~10之间，间隔2个取数
msg = "hello world"
for i in range(0,10,2):
    print(i,msg)
print()

# 从0~10之间，间隔1个取数
for i in range(10):
    print(i,msg)
print()

i = 1
for j in ('Beijing','Hongkong','London','Pairs','Berlin','Newyork','Tokyo','Seoul','Rome','Moscow'):
    print(i,j)
    i=i+1
