from distutils.cmd import Command
from tkinter import *

def btnClicked():
    cd = float(entryCd.get())   # 获取输入的设施温度
    fd = cd * 1.8 + 32          # 将摄氏温度转化为华氏温度
    label1.config(text = "%.2f ℃ = %.2f ℉" %(cd, fd))   # 按指定格式显示两个温度

root = Tk()   # 创建一个简单的窗口
root.title("摄氏温度转华氏温度")  # 给窗口命名

label1 = Label(root,text="摄氏温度转华氏温度", height = 5, width = 40, fg = "blue")
entryCd = Entry(root, text = "0")
btnCal = Button(root, text = "转换", command = btnClicked)

label1.pack()
entryCd.pack()
btnCal.pack()

root.mainloop()
