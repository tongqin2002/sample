# 对象和类
class Dog():
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def sit(self):
        print(self.name.title(),"蹲下!")

    def roll_over(self):
        print(self.name.title(),"打滚！")

dog1 = Dog("阿黄","黄色")
print("小狗名叫：" + dog1.name,"颜色为：" + dog1.color)
dog1.sit()

dog2 = Dog("阿美","白色")
print("小狗名叫：" + dog2.name,"颜色为：" + dog2.color)
dog2.roll_over()
