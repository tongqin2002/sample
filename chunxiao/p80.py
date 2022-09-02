# 找出100以内的能够被3整除的正整数（方法1）
aliq = []
for n in range(1, 101):
    if n%3 == 0:
        aliq.append(n)
print(aliq)

# 找出100以内的能够被3整除的正整数（方法2）
for n in range(3, 101,3):
    print(n,end=' ')  # python默认以换行结尾，这里指定为空格结尾

print()  #换行

#编程求解鸡兔同笼问题
heads = 35
legs = 94
for i in range(1,heads + 1):
    if i * 2 + (heads - i) * 4 == legs:
        print("chickens:",i)
        print("rabits:",35-i)
