# 从0~10之间，间隔2个取数
msg = "hello world"
for i in range(0,10,2):
    print(i,msg)
print()

# 从0~10之间，间隔1个取数
for i in range(10):
    print(i,msg)
print()
  
# 测试嵌套循环
for i in range(5):
    for j in range(3):
        print(i,j)
print()

# 定义列表
arr = ('Beijing','Hongkong','London','Pairs','Berlin','Newyork','Tokyo','Seoul','Rome','Moscow')
# 打印列表
print(arr)
# 轮询列表
for index, value in enumerate(arr):
    print(index, value)
print()