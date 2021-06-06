import tkinter as tk
from tkinter import filedialog
from tkinter.constants import NONE
from PIL import Image,ImageTk
import cv2 as cv
#调用库函数
win=tk.Tk()
win.title('实验二')
win.geometry('1024x1024')
#建立窗口
class PictureProcess():    
    def selectPicture(self):
        pic_name = filedialog.askopenfilename(title='选择图片', filetypes=[('jpg','png'), ('All Files', '*')])
        return pic_name
    def add_together(self,r_a,r_b):
        image_add=cv.add(r_a,r_b)       
        cv.imwrite('add.png',image_add)
        path_add='add.png'
        return path_add
    def subtract_together(self,r_a,r_b):
        image_subtract=cv.subtract(r_a,r_b)
        cv.imwrite('subtract.png',image_subtract) 
        path_subtract='subtract.png'
        return path_subtract 
    def multiply_together(self,r_a,r_b):
        image_multiply=cv.multiply(r_a,r_b)
        cv.imwrite('multiply.png',image_multiply)
        path_multiply='multiply.png'
        return path_multiply
    def divide_together(self,r_a,r_b):
        image_divide=cv.divide(r_a,r_b)
        cv.imwrite('divide.png',image_divide)
        path_divide='divide.png'
        return path_divide      
#图片处理过程使用面向对象编程
Pic=PictureProcess()
Pic1=PictureProcess()
Pic2=PictureProcess()
#建立两个对象分别对应进行处理的两张图片
def pic_select_a(): 
    global photo_a,path_a    #若需在方法中调用图片，则需提前声明全局变量
    path_a=Pic1.selectPicture()
    image_a=Image.open(path_a)  
    photo_a = ImageTk.PhotoImage(image_a)
    l_1=tk.Label(win, image=photo_a)
    l_1.grid(row=2,column=1)
botton1=tk.Button(win,text='选择图片a',width=10,height=2,command=pic_select_a)
botton1.grid(row=1,column=1)
#建立选择图片a按钮及其功能
def pic_select_b(): 
    global photo_b,path_b
    path_b=Pic2.selectPicture()    
    image_b=Image.open(path_b)
    r_b=cv.imread(path_b)
    photo_b = ImageTk.PhotoImage(image_b)
    l_2=tk.Label(win, image=photo_b)
    l_2.grid(row=2,column=2)
botton2=tk.Button(win,text='选择图片b',width=10,height=2,command=pic_select_b)
botton2.grid(row=1,column=2)
#建立选择图片b按钮及其功能
def pic_add():
    global photo_add,r_a
    r_a=cv.imread(path_a)
    r_b=cv.imread(path_b)
    image_add_re=Image.open(Pic.add_together(r_a,r_b))
    photo_add=ImageTk.PhotoImage(image_add_re)
    l_add=tk.Label(win,image=photo_add)
    l_add.grid(row=4,column=1)
botton3=tk.Button(win,text='图片相加',width=10,height=2,command=pic_add)
botton3.grid(row=3,column=1)
#建立图片相加按钮及其功能
def pic_subtract():
    global photo_subtract
    r_a=cv.imread(path_a)
    r_b=cv.imread(path_b)
    image_subtract_re=Image.open(Pic.subtract_together(r_a,r_b))
    photo_subtract=ImageTk.PhotoImage(image_subtract_re)
    l_subtract=tk.Label(win,image=photo_subtract)
    l_subtract.grid(row=4,column=2)
botton4=tk.Button(win,text='图片相减',width=10,height=2,command=pic_subtract)
botton4.grid(row=3,column=2)
#建立图片相减按钮及其功能
def pic_multiply():
    global photo_multiply
    r_a=cv.imread(path_a)
    r_b=cv.imread(path_b)
    image_multiply_re=Image.open(Pic.multiply_together(r_a,r_b))
    photo_multiply=ImageTk.PhotoImage(image_multiply_re)
    l_multiply=tk.Label(win,image=photo_multiply)
    l_multiply.grid(row=4,column=3)
botton5=tk.Button(win,text='图片相乘',width=10,height=2,command=pic_multiply)
botton5.grid(row=3,column=3)
def pic_divide():
    global photo_divide
    r_a=cv.imread(path_a)
    r_b=cv.imread(path_b)
    image_divide_re=Image.open(Pic.divide_together(r_a,r_b))
    photo_divide=ImageTk.PhotoImage(image_divide_re)
    l_divide=tk.Label(win,image=photo_divide)
    l_divide.grid(row=4,column=4)
botton6=tk.Button(win,text='图片相除',width=10,height=2,command=pic_divide)
botton6.grid(row=3,column=4)
win.mainloop()