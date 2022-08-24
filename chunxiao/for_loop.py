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

"""
定义元组arr
元组()和列表[]的不同之处在于：
列表的元素是可以更改的，包括修改元素值，删除和插入元素，所以列表是可变序列；
而元组一旦被创建，它的元素就不可更改了，所以元组是不可变序列
"""
arr = ('Beijing','Hongkong','London','Pairs','Berlin','Newyork','Tokyo','Seoul','Rome','Moscow')
# 打印元组
print(arr)
# 轮询元组
for index, value in enumerate(arr):
    print(index, value)
print()